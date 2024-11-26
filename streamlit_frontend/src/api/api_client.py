# src/api/api_client.py
import requests

class APIClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
    
    def process_image(self, image_file):
        url = f"{self.base_url}/ocr/process"
        files = {"file": image_file}
        response = requests.post(url, files=files)
        return response.json()
    
    def process_text(self, text):
        url = f"{self.base_url}/llm/process"
        response = requests.post(url, json={"text": text})
        return response.json()