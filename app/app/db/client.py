from pymongo import MongoClient
from app.core.config import settings

client = MongoClient(
    settings.DB_HOST,
    settings.DB_PORT,
    username=settings.DB_USER,
    password=settings.DB_PASSWORD,
)
