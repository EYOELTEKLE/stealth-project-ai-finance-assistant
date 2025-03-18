import os

import requests
from app.services.ai_service import analyze_news_sentiment, investment_advice
from app.services.email_service import send_insight_email
from app.infrastructure.financial_data import get_stock_price, get_news
import asyncio
# def get_stock_price(symbol="AAPL"):
#     """Fetch stock price (mocked function, replace with real API)"""
#     return {"symbol": symbol, "price": 180.5}  # Mocked data
#
# def get_news(symbol="AAPL"):
#     """Fetch financial news (mocked function, replace with real API)"""
#     return [{"title": f"Stock market update for {symbol}"}]  # Mocked news

async def scheduled_stock_analysis():
    """Fetch stock data, analyze news, and provide investment advice."""
    symbol = "AAPL"

    stock_data = await get_stock_price(symbol)
    print(stock_data,"stock data")
    news_articles =await get_news(symbol)

    if not stock_data or not news_articles:
        print("[ERROR] Stock data or news unavailable.")
        return

    print(stock_data,news_articles,"results of API")
    # AI News Sentiment Analysis
    top_news = news_articles[0]['title'] if news_articles else "No recent news."
    sentiment = await analyze_news_sentiment(top_news)

    print(sentiment,"AI SENTIMENT")
    # AI Investment Advice
    recommendation = await investment_advice({
        "symbol": symbol,
        "price": stock_data.get("price"),
        "trend": sentiment
    })

    print(recommendation,"AI ADVICE")
    # Generate Email Content
    # email_body = f"""
    #    <h2>📈 Investment Insights for {symbol}</h2>
    #    <p>🔹 <b>Stock Price:</b> ${stock_data['price']}</p>
    #    <p>📰 <b>Top News:</b> {top_news}</p>
    #    <p>📊 <b>Sentiment:</b> {sentiment}</p>
    #    <p>💡 <b>Recommendation:</b> {recommendation}</p>
    #    """

    print("🚀 Sending Email Notification...")
    await send_insight_email(os.getenv("RECEIVER_EMAIL"), f"📢 {symbol} Stock Insights", recommendation)
