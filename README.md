# News Collection System

A serverless AWS Lambda-based system for fetching and storing news articles in an S3 bucket and DynamoDB using the News API.

## Features
- Fetches news articles from NewsAPI.
- Stores metadata in **DynamoDB**.
- Saves article content to **AWS S3**.
- Uses **AWS Lambda** for automated execution.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- AWS CLI configured with valid credentials
- Dependencies installed via `requirements.txt`
- API Key for [NewsAPI](https://newsapi.org/)

## Project Structure
```
news-collection-service/
|-- .env
|-- config.py
├── requirements.txt             # Dependencies for Python 
├── app/
│   ├── __init__.py
│   ├── news_api_client.py       # Handles NewsAPI integration
│   ├── dynamodb_handler.py      # Handles DynamoDB interactions
│   ├── s3_handler.py            # Handles S3 interactions
│   ├── lambda_function.py       # Entry point for AWS Lambda
│   ├── utils.py                 # Utility functions (e.g., UUID generation)
├── deploy/
│   ├── template.yaml            # AWS SAM template for deployment
│   ├── deploy.sh                # Deployment script using AWS SAM


```

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/aniketp166/NewsCollectionService.git
   cd NewsCollectionService
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add:
   ```
   NEWS_API_KEY=your-api-key
   AWS_ACCESS_KEY_ID=your-aws-key
   AWS_SECRET_ACCESS_KEY=your-aws-secret
   AWS_REGION=your-region
   S3_BUCKET_NAME=your-bucket-name
   DYNAMODB_TABLE_NAME=your-table-name
   ```

## Usage

### Running Locally
To test locally:
```sh
python app/lambda_function.py
```
