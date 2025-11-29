import streamlit as st
import pandas as pd
import os
import kagglehub
from dotenv import load_dotenv
from pathlib import Path
import google.generativeai as genai

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

st.title("Chat with YouTube Analytics Data")

# Get API Key from environment
api_key = os.getenv("GOOGLE_API_KEY")

# Debug: Check if .env file exists and what we loaded
if not api_key:
    st.error(f"GOOGLE_API_KEY not found in environment variables.")
    st.write(f"Looking for .env at: {env_path.absolute()}")
    st.write(f".env exists: {env_path.exists()}")
    if env_path.exists():
        with open(env_path) as f:
            st.write(f".env content preview: {f.read()[:50]}...")
    st.info("Get a free API key from: https://makersuite.google.com/app/apikey")
else:
    # Configure Gemini API
    genai.configure(api_key=api_key)

    # Load Data
    @st.cache_data
    def load_data():
        path = kagglehub.dataset_download("shaistashahid/youtube-analytics-data")
        csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
        if csv_files:
            return pd.read_csv(os.path.join(path, csv_files[0]))
        return None

    df = load_data()

    if df is not None:
        st.write("### Dataset Preview")
        st.write(df.head())

        # Chat Interface
        query = st.text_area("Ask a question about the data:")
        
        if query:
            if st.button("Ask"):
                # Create a context about the data for Gemini
                df_summary = f"""
                Dataset Information:
                - Shape: {df.shape}
                - Columns: {list(df.columns)}
                - Data Types: {df.dtypes.to_dict()}
                - First few rows:
                {df.head(10).to_string()}
                """
                
                # Use Gemini to answer questions about the data
                model = genai.GenerativeModel('gemini-2.5-pro')
                prompt = f"""You are a data analyst. Based on the following dataset information, answer the user's question.

{df_summary}

User question: {query}

Provide a clear and concise answer based on the data shown above."""
                
                response = model.generate_content(prompt)
                st.write("### Answer")
                st.write(response.text)
    else:
        st.error("Could not load dataset.")
