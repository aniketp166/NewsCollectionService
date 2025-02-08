import requests
from config import Config

NEWS_API_BASE_URL = "https://newsapi.org/v2/top-headlines"

def fetch_news(country="in", category=None, page_size=5):
    """Fetch news articles from NewsAPI with proper error handling."""
    params = {
        "apiKey": Config.NEWS_API_KEY,
        "country": country,
        "category": category,
        "pageSize": page_size  
    }
    
    try:
        response = requests.get(NEWS_API_BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json().get("articles", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []
