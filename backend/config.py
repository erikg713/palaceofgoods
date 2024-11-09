import os
from dotenv import load_dotenv

ENVIRONMENT = os.getenv("FLASK_ENV", "development")
dotenv_path = f".env.{ENVIRONMENT}"
load_dotenv(dotenv_path)

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    CORS_HEADERS = 'Content-Type'
