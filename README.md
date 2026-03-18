# ⚡ CLAW X — AI Crypto Management Agent

> **Built for the Binance Contest** · Powered by Binance API · DeepSeek AI via OpenRouter

CLAW X is a web-based AI agent for crypto management. It combines real-time market data, on-chain analytics, and LLM-powered intelligence into a single trading dashboard.

---

## 🎯 What It Does

| Skill | Description |
|---|---|
| 💬 **AI Chat** | Natural language crypto assistant powered by DeepSeek |
| 📈 **DCA Signals** | RSI + MACD powered buy/hold/sell signals |
| 🛡️ **Smart Exit** | Stop-loss, take-profit and trailing stop rules |
| 🐋 **Whale Alerts** | Real on-chain large transaction monitoring |
| 🔔 **Price Alerts** | Custom price notifications via Telegram |
| 📢 **Binance News** | Real-time Binance announcements from 6 sources |
| 📰 **News Feed** | Live crypto news from CoinTelegraph + CoinDesk |
| 🔍 **Narrative Scan** | Fear & Greed Index + AI market narrative analysis |
| 👛 **Wallet Tracker** | Track whale wallets on-chain via Etherscan |

---

## 🏗️ Project Structure

```
claw-x/
│
├── app.py                  # Main Streamlit app — all 9 skills
├── aurora.py               # Visual theme — Gold Amber skin
│
├── utils/
│   ├── __init__.py
│   ├── exchange.py         # Binance/ccxt price fetching
│   └── llm.py              # OpenRouter LLM helper
│
├── config/
│   └── settings.py         # Environment variable loader
│
├── tests/
│   ├── test_connection.py  # Binance connection test
│   └── test_telegram.py    # Telegram bot test
│
├── .env.example            # Environment variables template
├── .gitignore              # Ignored files
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🔧 Tech Stack

```
Frontend    → Streamlit (Python web UI)
AI/LLM      → DeepSeek V3 via OpenRouter API
Exchange    → Binance via ccxt
Indicators  → RSI, MACD (numpy + pandas)
News        → CryptoPanic, CoinTelegraph, CoinDesk RSS
On-chain    → Blockchair API, Etherscan API, Whale Alert TG
Sentiment   → Fear & Greed Index (alternative.me)
Alerts      → Telegram Bot API
Scraping    → BeautifulSoup4, feedparser
```

---

## ⚙️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      CLAW X APP                         │
│                                                         │
│  ┌──────────┐   ┌──────────────────────────────────┐   │
│  │          │   │           SKILLS                  │   │
│  │ SIDEBAR  │──▶│  DCA · Exit · Whale · Alerts      │   │
│  │   NAV    │   │  News · Narrative · Wallet        │   │
│  │          │   └──────────────┬───────────────────┘   │
│  └──────────┘                  │                        │
│                                ▼                        │
│  ┌─────────────────────────────────────────────────┐   │
│  │              DATA LAYER                          │   │
│  │                                                  │   │
│  │  Binance API   OpenRouter LLM   Blockchair API   │   │
│  │  CryptoPanic   Etherscan API    Fear&Greed API   │   │
│  │  CoinTelegraph RSS   Binance TG   Whale Alert TG │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │              NOTIFICATIONS                       │   │
│  │           Telegram Bot API                       │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/claw-x.git
cd claw-x
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
```bash
cp .env.example .env
nano .env  # Fill in your API keys
```

### 5. Run the app
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🔑 Environment Variables

```bash
# Required
OPENROUTER_API_KEY=        # Get from openrouter.ai

# Optional — for live trading (dry run by default)
BINANCE_API_KEY=
BINANCE_SECRET=

# Optional — for Telegram notifications
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=

# Optional — for Wallet Tracker
ETHERSCAN_API_KEY=
ALCHEMY_API_KEY=
```

---

## 📦 Requirements

```
streamlit
ccxt
pandas
numpy
requests
feedparser
python-dotenv
beautifulsoup4
altair
apscheduler
cryptography
vaderSentiment
```

---

## 🏆 Built For

**Binance Contest 2025** — AI-powered crypto management tools built on Binance infrastructure.

---

## ⚠️ Disclaimer

CLAW X runs in **DRY RUN mode** by default. No real trades are executed without explicit configuration. This is not financial advice.

---

<div align="center">
  <img src="https://bin.bnbstatic.com/static/images/common/favicon.ico" width="20"/>
  <strong> POWERED BY BINANCE</strong>
</div>
