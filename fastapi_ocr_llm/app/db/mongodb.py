# app/db/mongodb.py
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGODB_URL

client = AsyncIOMotorClient(MONGODB_URL)
database = client.your_database_name

async def connect_to_mongo():
    try:
        await client.admin.command('ping')
        print("Connected to MongoDB")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

async def close_mongo_connection():
    client.close()