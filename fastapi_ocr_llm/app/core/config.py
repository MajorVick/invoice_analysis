# app/core/config.py
import os

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
LLM_API_KEY = os.getenv("LLM_API_KEY", "your-api-key")