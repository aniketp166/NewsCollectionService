import boto3
import json
from botocore.exceptions import ClientError
from config import Config

s3 = boto3.client(
    's3',
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.AWS_REGION,
    endpoint_url=Config.AWS_ENDPOINT_URL
)

def create_bucket():
    """Creates an S3 bucket if it doesn't exist."""
    try:
        s3.create_bucket(Bucket=Config.S3_BUCKET_NAME)
        print(f"S3 bucket '{Config.S3_BUCKET_NAME}' created successfully.")
    except ClientError as e:
        if e.response["Error"]["Code"] == "BucketAlreadyOwnedByYou":
            print(f"S3 bucket '{Config.S3_BUCKET_NAME}' already exists.")
        else:
            print(f"Error creating bucket: {e}")

def archive_article(article, article_id):
    """Saves the article content in S3 as a JSON file."""
    if not article_id:
        print("Invalid article ID. Skipping archiving.")
        return

    file_name = f"{article_id}.json"
    try:
        article_json = json.dumps(article)
        s3.put_object(
            Bucket=Config.S3_BUCKET_NAME,
            Key=file_name,
            Body=article_json,
            ContentType="application/json"
        )
        print(f"Archived article '{article['title']}' to S3 as {file_name}")
    except ClientError as e:
        print(f"Error archiving article: {e}")
