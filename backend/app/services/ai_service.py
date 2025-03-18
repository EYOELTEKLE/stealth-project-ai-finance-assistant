import google.generativeai as genai

import os
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")
async def analyze_news_sentiment(news_text: str):
    """AI analyzes news sentiment."""

    response = model.generate_content([
        f"Analyze sentiment for this financial news: '{news_text}' and classify as Positive, Neutral, or Negative."
    ])
    print(response.text)
    return response.text

async def investment_advice(stock_data):
    """AI provides investment recommendations."""
    prompt = f"""
    Analyze stock data and recommend an action:
    Stock: {stock_data['symbol']}
    Price: {stock_data['price']}
    Trend: {stock_data['trend']}

    Respond in JSON:
    {{
        "recommendation": "Buy/Sell/Hold",
        "justification": "string",
        "risk_assessment": "Low/Medium/High"
    }}
    """
    response = model.generate_content([prompt])
    print(response.text)
    return response.text
