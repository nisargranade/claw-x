# utils/exchange.py
import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

def get_exchange():
    return ccxt.binance({
        "apiKey": os.getenv("BINANCE_API_KEY", ""),
        "secret": os.getenv("BINANCE_SECRET", ""),
        "enableRateLimit": True,
        "options": {
            "defaultType": "spot",
            "adjustForTimeDifference": True,
        },
    })

def get_price(symbol: str) -> float:
    """Fetch price — works WITHOUT API keys."""
    exchange = ccxt.binance({"enableRateLimit": True})  # public only
    ticker = exchange.fetch_ticker(symbol)
    return ticker["last"]

def fetch_ohlcv(symbol: str, timeframe: str = "1h", limit: int = 100) -> list:
    """Fetch candle data — works WITHOUT API keys."""
    exchange = ccxt.binance({"enableRateLimit": True})  # public only
    return exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
