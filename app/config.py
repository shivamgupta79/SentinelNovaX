import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/sentinel")
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
