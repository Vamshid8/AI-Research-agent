# Patent Innovation Predictor
A powerful agentic AI system for patent trend analysis and future technology prediction using Ollama, OpenSearch, and CrewAI.

### Overview
This system analyzes patent data to identify trends and predict future innovations in specific technology areas (with a focus on lithium battery technology). It uses a multi-agent approach with specialized roles for research direction, patent retrieval, data analysis, and innovation forecasting.

### System Architecture

┌───────────────────────────────────────────────────────────────┐
│                     User Interface Layer                      │
└───────────────────────────────────────────────────────────────┘
                │                │                │
                ▼                ▼                ▼
┌───────────────────────────────────────────────────────────────┐
│                     Agent Orchestration Layer                 │
│  ┌──────────────────┐   ┌────────────────┐  ┌───────────────┐ │
│  │ Research Director│   │Patent Retriever│  │Data Analyst   │ │
│  └──────────────────┘   └────────────────┘  └───────────────┘ │
│                                                               │
│  ┌──────────────────┐                                         │
│  │Innovation        │                                         │
│  │Forecaster        │                                         │
│  └──────────────────┘                                         │
└───────────────────────────────────────────────────────────────┘
                │                │                │
                ▼                ▼                ▼
┌───────────────────────────────────────────────────────────────┐
│                   Knowledge Processing Layer                  │
│  ┌───────────────┐    ┌───────────────┐    ┌───────────────┐  │
│  │ Semantic      │    │ Hybrid        │    │ Iterative     │  │
│  │ Search        │    │ Search        │    │ Search        │  │
│  └───────────────┘    └───────────────┘    └───────────────┘  │
└───────────────────────────────────────────────────────────────┘
                │                │                │
                ▼                ▼                ▼
┌───────────────────────────────────────────────────────────────┐
│                        Data Storage Layer                     │
│  ┌───────────────────────────────────────────────────────────┐│
│  │                       OpenSearch                          ││
│  └───────────────────────────────────────────────────────────┘│
└───────────────────────────────────────────────────────────────┘

### Prerequisites
- Python 3.10+
- Ollama for running local LLM models
- OpenSearch instance running (default: localhost:9200)
- Access to patent data (pre-loaded in OpenSearch)

### Installation
1. Clone the repository:
```
git clone https://github.com/yesdeepakmittal/product-research-ai-agent.git
cd product-research-ai-agent
```

2. Create a virtual environment:
```python
python -m venv .venv
source .venv/bin/activate 
```

3. Install dependencies:
```python
pip install -r requirements.txt
```

4. Install and start Ollama:
```
ollama serve
```

5. Pull required models:
```
ollama pull llama2  # For general agent tasks
ollama pull nomic-embed-text  # For embeddings
```

6. Start OpenSearch: Make sure your OpenSearch instance is running on localhost:9200 (or update the connection settings in the code).

### Configuration
1. Environment variables (optional): Create a .env file for any API keys or configuration:
```
# Optional API keys
SERPAPI_API_KEY=your_key_here
```

2. OpenSearch setup: The system will automatically create necessary indices if they don't exist.

### Usage
Run the main application:
```
python patent_analyzer_app.py
```

The application presents a menu with options:

1. Run complete patent trend analysis and forecasting:
- Executes the full multi-agent workflow
- Outputs comprehensive analysis and predictions
- Saves results to a text file

2. Search for specific patents:
- Search by keyword
- Search by semantic similarity
- Search by hybrid approach (combining both)

3. Iterative patent exploration:
- Performs step-by-step refinement of search queries
- Discovers related patents and technologies

4. View system status:
- Checks OpenSearch connection
- Verifies Ollama availability and models
- Tests embedding functionality

### Example Workflow
- Start the application
- Choose option 4 to verify system status
- Choose option 1 to run complete analysis
- Enter research area (e.g., "Lithium Battery")
- Select an available Ollama model (e.g., "llama2")
- Review and save the analysis results