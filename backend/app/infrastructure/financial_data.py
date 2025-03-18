import requests
import os
import asyncio
ALPHA_VANTAGE_API_KEY=os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY=os.getenv("NEWS_API_KEY")
async def get_stock_price(ticker: str):
    """Fetch stock price from Alpha Vantage."""
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data.get("Global Quote", {})

async def get_news(query: str):
    """Fetch financial news headlines."""
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return response.json().get("articles", [])
