import boto3
from uuid import uuid4
from datetime import datetime
from botocore.exceptions import ClientError
from config import Config

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.AWS_REGION,
    endpoint_url=Config.AWS_ENDPOINT_URL
)

table_name = Config.DYNAMODB_TABLE_NAME

def store_metadata(article):
    """Store article metadata in DynamoDB."""
    article_id = str(uuid4())
    try:
        table = dynamodb.Table(table_name)
        item = {
            "article_id": article_id,
            "title": article["title"],
            "source": article["source"].get("name", "Unknown"),
            "published_at": article.get("publishedAt", ""),
            "url": article.get("url", ""),
            "summary": article.get("description", ""),
            "topics": [],  
            "stored_at": datetime.utcnow().isoformat()
        }
        table.put_item(Item=item)
        return article_id
    except ClientError as e:
        print(f"Error storing metadata: {e}")
        return None

def create_table():
    """Creates the DynamoDB table if it doesn't exist."""
    try:
        existing_tables = [t.name for t in dynamodb.tables.all()]
        if table_name in existing_tables:
            print(f"Table {table_name} already exists.")
            return

        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{"AttributeName": "article_id", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "article_id", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}
        )
        table.wait_until_exists()
        print(f"Table {table_name} created successfully.")
    except ClientError as e:
        print(f"Error creating table: {e}")
