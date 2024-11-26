# app/main.py
from fastapi import FastAPI
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.services.ocr import ocr_service
from app.services.llm import llm_service

app = FastAPI()

@app.on_event("startup")
async def startup():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection()

# Add your routes here