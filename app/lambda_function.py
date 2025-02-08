import sys
import os
from config import Config

sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from news_api_client import fetch_news
from dynamodb_handler import store_metadata, create_table  
from s3_handler import archive_article, create_bucket  

def lambda_handler(event, context):
    """AWS Lambda function to fetch, store, and archive news articles."""
    create_table()  
    create_bucket()

    articles = fetch_news(country="in")

    if not articles:
        print("No articles found.")
        return {"statusCode": 500, "body": "No articles retrieved"}

    for article in articles:
        try:
            article_id = store_metadata(article)
            if article_id:
                archive_article(article, article_id)
                print(f"Processed article: {article['title']}")
        except Exception as e:
            print(f"Error processing article: {e}")

    return {"statusCode": 200, "body": "Articles processed successfully"}
