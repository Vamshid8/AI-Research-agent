import streamlit as st
from patent_crew import run_patent_analysis
from datetime import datetime

# --- Streamlit App Configuration ---
st.set_page_config(
    page_title="Product Research AI Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- App Styling ---
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        background-color: #f1f1f1;
        color: black;
    }
</style>
""", unsafe_allow_html=True)


# --- Main Application ---
st.title("🔬 Product Research AI Agent")
st.markdown("Enter a research topic and an Ollama model to generate a patent analysis report.")

# --- Sidebar for Inputs ---
with st.sidebar:
    st.header("⚙️ Configuration")
    research_area = st.text_input(
        "Enter Research Area:", 
        value="Generative AI",
        help="e.g., 'lithium batteries', 'quantum computing', 'gene editing'"
    )
    model_name = st.text_input(
        "Enter Ollama Model Name:", 
        value="llama2",
        help="e.g., 'llama3', 'mistral', 'deepseek-r1:1.5b'"
    )
    start_button = st.button("Start Analysis")


# --- Main Content Area for Output ---
if start_button:
    if not research_area:
        st.error("Please enter a research area.")
    elif not model_name:
        st.error("Please enter a model name.")
    else:
        st.info(f"Running analysis for '{research_area}' using model '{model_name}'. Please wait...")
        
        with st.spinner("The AI crew is analyzing patents... This may take several minutes."):
            try:
                # Run the patent analysis crew
                result = run_patent_analysis(research_area, model_name)
                
                st.success("Analysis complete!")
                st.subheader("Patent Analysis Report")
                st.markdown(result)
                
                # Save results to file
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"patent_analysis_{timestamp}.txt"
                with open(filename, "w") as f:
                    f.write(result)
                st.info(f"Report saved to {filename}")

            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
else:
    st.info("Enter your research topic and model in the sidebar and click 'Start Analysis'.")

# --- Footer ---
st.markdown("---")
st.markdown("Powered by CrewAI and Streamlit") 