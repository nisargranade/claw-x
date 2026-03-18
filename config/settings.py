# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
BINANCE_API_KEY    = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET     = os.getenv("BINANCE_SECRET")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID   = os.getenv("TELEGRAM_CHAT_ID")
DRY_RUN = True
