from embedding import get_embedding
from information_collector import fetch_patent_data
from ingestion import index_patent_data, load_patent_data
from opensearch_client import create_index_if_not_exists, get_opensearch_client


def hybrid_search(client, index_name, query_text, top_k=5):
    """
    Perform a hybrid search using both keyword and vector-based semantic search.

    Args:
        client: OpenSearch client instance
        index_name: Name of the index to search in
        query_text: Search query text
        top_k: Number of results to return

    Returns:
        list: Combined search results
    """
    # Get embedding for the query
    try:
        query_embedding = get_embedding(query_text)

        # Create a hybrid search query that combines:
        # 1. Semantic search using vector embeddings
        # 2. Keyword search using the abstract field
        search_query = {
            "size": top_k,
            "query": {
                "bool": {
                    "should": [
                        # Vector search for semantic matching
                        {"knn": {"embedding": {"vector": query_embedding, "k": top_k}}},
                        # Full-text search for keyword matching
                        {"match": {"abstract": query_text}},
                    ]
                }
            },
            "_source": ["title", "abstract", "publication_date", "patent_id"],
        }

        response = client.search(index=index_name, body=search_query)
        return response["hits"]["hits"]

    except Exception as e:
        print(f"Vector search error: {e}")
        print("Falling back to keyword-only search...")

        # Fallback to keyword-only search if vector search fails
        fallback_query = {
            "size": top_k,
            "query": {"match": {"abstract": query_text}},
            "_source": ["title", "abstract", "publication_date", "patent_id"],
        }

        try:
            response = client.search(index=index_name, body=fallback_query)
            return response["hits"]["hits"]
        except Exception as e2:
            print(f"Keyword search error: {e2}")
            return []


if __name__ == "__main__":
    # Fetch patent data for a specific query and save it to a directory
    dir_path = "results3"
    query = "lithium battery"
    # fetch_patent_data(query, dir_path)
    # print(f"Patent data for query '{query}' has been saved to '{dir_path}'.")

    # Initialize OpenSearch client
    host = "localhost"
    port = 9200
    client = get_opensearch_client(host, port)

    # Create index with proper mapping for vector search
    index_name = "patents"
    create_index_if_not_exists(client, index_name)

    # Load and index patent data
    try:
        patent_data = load_patent_data(dir_path)
        print(f"Loaded {len(patent_data)} patents from '{dir_path}'")

        # Index the data
        index_patent_data(client, index_name, patent_data)
        print(f"Indexed {len(patent_data)} patents into '{index_name}' index.")
    except Exception as e:
        print(f"Error loading or indexing data: {e}")

    # Perform hybrid search with user query
    user_query = input("Enter your search query: ")
    if not user_query:
        user_query = query

    print(f"\nSearching for: '{user_query}'")
    results = hybrid_search(client, index_name, user_query)

    # Print search results
    print(f"\nFound {len(results)} results:")
    print("-" * 80)
    for i, hit in enumerate(results):
        source = hit["_source"]
        print(f"{i+1}. {source['title']}")
        print(f"   Score: {hit['_score']}")
        print(f"   Date: {source.get('publication_date', 'N/A')}")
        print(f"   Patent ID: {source.get('patent_id', 'N/A')}")
        print(f"   Abstract: {source['abstract'][:200]}...")
        print("-" * 80)
