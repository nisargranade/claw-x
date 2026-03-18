import requests
import os
from dotenv import load_dotenv

load_dotenv()

token   = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

print(f"Token: {token[:20]}..." if token else "❌ No token found")
print(f"Chat ID: {chat_id}" if chat_id else "❌ No chat ID found")

r = requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    json={
        "chat_id": chat_id,
        "text": "🐾 OpenClaw AI connected!",
        "parse_mode": "Markdown"
    }
)
print(r.json())
