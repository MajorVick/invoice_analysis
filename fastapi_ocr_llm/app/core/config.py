# app/core/config.py
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
LLM_API_KEY = os.getenv("LLM_API_KEY")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"