from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME")
    S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.getenv('AWS_REGION')
    AWS_ENDPOINT_URL = os.getenv('AWS_ENDPOINT_URL', "http://localhost:4566")
