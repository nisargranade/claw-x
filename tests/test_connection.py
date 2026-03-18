# tests/test_connection.py
import sys
import os

# This tells Python where to find utils/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.exchange import get_price

price = get_price("BTC/USDT")
print(f"✅ Binance connected! BTC price: ${price:,.2f}")
