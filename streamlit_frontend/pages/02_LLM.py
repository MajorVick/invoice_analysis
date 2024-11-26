# pages/02_LLM.py
import streamlit as st
from src.api.api_client import APIClient

st.title("LLM Processing")

text_input = st.text_area("Enter text to process")
if text_input:
    if st.button("Process Text"):
        client = APIClient()
        result = client.process_text(text_input)
        st.write("LLM Response:")
        st.write(result["response"])