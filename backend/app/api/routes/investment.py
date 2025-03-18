from fastapi import APIRouter, Query
from app.infrastructure.financial_data import get_stock_price, get_news
from app.services.ai_service import analyze_news_sentiment, investment_advice

router = APIRouter()

@router.get("/investment/{ticker}")
async def investment_recommendation(ticker: str):
    """Fetch stock data, analyze news, and give AI-powered investment advice."""
    stock_data = get_stock_price(ticker)
    news_articles = get_news(ticker)

    if not stock_data or not news_articles:
        return {"error": "Stock data or news unavailable"}

    # AI News Sentiment Analysis
    top_news = news_articles[0]['title'] if news_articles else "No recent news."
    sentiment = await analyze_news_sentiment(top_news)

    # AI Investment Advice
    recommendation = await investment_advice({
        "symbol": ticker,
        "price": stock_data.get("05. price"),
        "trend": sentiment
    })

    return {
        "stock_data": stock_data,
        "top_news": top_news,
        "news_sentiment": sentiment,
        "investment_advice": recommendation
    }
