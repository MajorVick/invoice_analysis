# pages/01_OCR.py
import streamlit as st
from src.api.api_client import APIClient

st.title("OCR Processing")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    if st.button("Process Image"):
        client = APIClient()
        result = client.process_image(uploaded_file)
        st.write("Processed Text:")
        st.write(result["text"])