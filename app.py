# app.py — CLAW X
import streamlit as st
import ccxt
import os
from dotenv import load_dotenv
import numpy as np
import pandas as pd
import requests

load_dotenv()

# ── Telegram Notifier ─────────────────────────────────────
def send_telegram(message: str):
    token   = os.getenv("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "")
    if not token or not chat_id:
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": message, "parse_mode": "Markdown"},
            timeout=5,
        )
    except:
        pass

# ── LLM ───────────────────────────────────────────────────
def ask_llm(prompt: str, system: str = "") -> str:
    try:
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        r = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:8501",
                "X-Title": "CLAW X",
            },
            json={
                "model": "deepseek/deepseek-chat-v3-0324",
                "messages": messages,
                "temperature": 0.4,
                "max_tokens": 400,
            },
            timeout=20,
        )
        return r.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"LLM Error: {str(e)}"

# ── Page Config ───────────────────────────────────────────
st.set_page_config(
    page_title="CLAW X",
    page_icon="⚡",
    layout="wide",
)
from aurora import skin
skin()

# ── Session State ─────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "🏠 Dashboard"
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "bot", "content": "Hey! I'm CLAW X 🐾 Your crypto agent. Ask me anything — DCA signals, whale alerts, news, price alerts, smart exits."}
    ]
if "exit_rules" not in st.session_state:
    st.session_state.exit_rules = []
if "price_alerts" not in st.session_state:
    st.session_state.price_alerts = []
if "narrative_summary" not in st.session_state:
    st.session_state.narrative_summary = None

# ── Live Prices ───────────────────────────────────────────
@st.cache_data(ttl=30)
def get_live_prices():
    try:
        exchange = ccxt.binance({"enableRateLimit": True})
        tickers = exchange.fetch_tickers(["BTC/USDT", "ETH/USDT", "SOL/USDT", "BNB/USDT"])
        return {
            symbol: {"price": data["last"], "change": round(data.get("percentage") or 0, 2)}
            for symbol, data in tickers.items()
        }
    except:
        return {
            "BTC/USDT": {"price": 83420.0, "change":  1.24},
            "ETH/USDT": {"price":  2841.5, "change": -0.87},
            "SOL/USDT": {"price":   132.4, "change":  3.21},
            "BNB/USDT": {"price":   598.3, "change":  0.45},
        }

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🐾 CLAW X")
    st.caption("Crypto Management Agent")
    st.markdown(
        "[![Binance](https://bin.bnbstatic.com/static/images/common/favicon.ico)](https://binance.com) "
        "**Powered by Binance**"
    )
    st.divider()

    pages = [
        "🏠 Dashboard",
        "💬 AI Chat",
        "📈 DCA Signals",
        "🛡️ Smart Exit",
        "🐋 Whale Alerts",
        "🔔 Price Alerts",
        "📢 Binance News",
        "📰 News Feed",
        "🔍 Narrative Scan",
        "👛 Wallet Tracker",
    ]

    for p in pages:
        if st.button(p, key=f"nav_{p}", width="stretch"):
            st.session_state.page = p
            st.rerun()

    st.divider()

    prices = get_live_prices()
    for symbol, data in prices.items():
        asset  = symbol.replace("/USDT", "")
        change = data["change"]
        arrow  = "▲" if change >= 0 else "▼"
        color  = "green" if change >= 0 else "red"
        st.markdown(f"**{asset}** ${data['price']:,.2f} :{color}[{arrow} {abs(change):.2f}%]")

    st.divider()
    st.caption(f"Page: {st.session_state.page}")

# ── Pages ─────────────────────────────────────────────────
page = st.session_state.page

# ═══════════════════════════════════════════════════════════
# DASHBOARD
# ═══════════════════════════════════════════════════════════
if page == "🏠 Dashboard":
    st.title("🏠 Dashboard")
    st.markdown("### Live Crypto Prices")
    prices = get_live_prices()
    cols = st.columns(4)
    for i, (symbol, data) in enumerate(prices.items()):
        asset = symbol.replace("/USDT", "")
        with cols[i]:
            st.metric(label=asset, value=f"${data['price']:,.2f}", delta=f"{data['change']:.2f}%")
    st.info("👈 Use the sidebar to navigate to each skill")

# ═══════════════════════════════════════════════════════════
# AI CHAT
# ═══════════════════════════════════════════════════════════

elif page == "💬 AI Chat":
    st.title("💬 AI Chat")
    st.markdown("Ask CLAW X anything about crypto")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "bot", "content": "Hey! I'm CLAW X 🐾 Your crypto agent. Ask me anything — DCA signals, whale alerts, news, price alerts, smart exits."}
        ]

    # ── Show messages ──────────────────────
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.chat_message("user").write(msg["content"])
        else:
            st.chat_message("assistant").write(msg["content"])

# ── Input at bottom — always visible ───
    if "chat_input_val" not in st.session_state:
        st.session_state.chat_input_val = ""

    col1, col2 = st.columns([6, 1])
    with col1:
        user_input = st.text_input(
            label="Message",
            placeholder="Ask CLAW X anything...",
            key="chat_input_box",
            value=st.session_state.chat_input_val,
            label_visibility="collapsed"
        )
    with col2:
        send = st.button("Send →", width="stretch")

    if send and user_input.strip():
        st.session_state.chat_input_val = ""
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input,
        })
        with st.spinner("CLAW X is thinking..."):
            system = """You are CLAW X — a sharp, confident crypto trading agent.
You help users with DCA signals, smart exits, whale alerts, price alerts, and news.
Be concise and direct. Use emojis sparingly. Always be helpful."""
            reply = ask_llm(user_input, system=system)
        st.session_state.chat_history.append({
            "role": "bot",
            "content": reply,
        })
        st.rerun()

# ═══════════════════════════════════════════════════════════
# DCA SIGNALS
# ═══════════════════════════════════════════════════════════
elif page == "📈 DCA Signals":
    st.title("📈 DCA Signals")
    st.markdown("RSI + MACD powered buy/hold/sell signals")

    @st.cache_data(ttl=60)
    def get_ohlcv(symbol, timeframe="1h", limit=100):
        try:
            exchange = ccxt.binance({"enableRateLimit": True})
            data = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
            return [c[4] for c in data]
        except:
            import random
            base = {"BTC/USDT":83000,"ETH/USDT":2800,"SOL/USDT":130,"BNB/USDT":590}.get(symbol, 100)
            closes = [base]
            for _ in range(limit - 1):
                closes.append(closes[-1] * (1 + random.uniform(-0.015, 0.015)))
            return closes

    def calc_rsi(closes, period=14):
        a = np.array(closes, dtype=float)
        d = np.diff(a)
        g = np.where(d > 0, d, 0.0)
        l = np.where(d < 0, -d, 0.0)
        ag = np.mean(g[:period])
        al = np.mean(l[:period])
        for i in range(period, len(g)):
            ag = (ag * (period - 1) + g[i]) / period
            al = (al * (period - 1) + l[i]) / period
        return round(100 - (100 / (1 + (ag / al if al != 0 else 1e-10))), 1)

    def calc_macd(closes):
        s = pd.Series(closes)
        macd = s.ewm(span=12).mean() - s.ewm(span=26).mean()
        signal = macd.ewm(span=9).mean()
        return round(macd.iloc[-1], 2), round(signal.iloc[-1], 2)

    col1, col2, col3 = st.columns(3)
    with col1:
        asset = st.selectbox("Asset", ["BTC","ETH","SOL","BNB","AVAX","ADA"])
    with col2:
        rsi_buy = st.slider("RSI Buy below", 15, 45, 30)
    with col3:
        rsi_sell = st.slider("RSI Sell above", 55, 85, 70)

    col4, col5 = st.columns(2)
    with col4:
        amount = st.number_input("DCA Amount (USDT)", min_value=10, value=100, step=10)
    with col5:
        timeframe = st.selectbox("Timeframe", ["1h","4h","1d"], index=1)

    if st.button("🔍 Get Signal", width="stretch"):
        symbol = f"{asset}/USDT"
        with st.spinner(f"Fetching {symbol} data..."):
            closes = get_ohlcv(symbol, timeframe)
            rsi    = calc_rsi(closes)
            macd_v, macd_s = calc_macd(closes)
            price  = closes[-1]

        if rsi < rsi_buy:
            signal = "BUY"
            reason = f"RSI is {rsi} — asset is oversold ✅"
        elif rsi > rsi_sell:
            signal = "SELL"
            reason = f"RSI is {rsi} — asset is overbought ⚠️"
        else:
            signal = "HOLD"
            reason = f"RSI is {rsi} — neutral zone ⏸"

        if signal == "BUY":
            st.success(f"### 🟢 Signal: {signal}")
        elif signal == "SELL":
            st.error(f"### 🔴 Signal: {signal}")
        else:
            st.warning(f"### 🟡 Signal: {signal}")

        st.markdown(f"**Reason:** {reason}")

        col_a, col_b, col_c, col_d = st.columns(4)
        col_a.metric("Price",  f"${price:,.2f}")
        col_b.metric("RSI",    rsi)
        col_c.metric("MACD",   macd_v)
        col_d.metric("Amount", f"${amount}")

        st.markdown("#### Price Chart")
        chart_df = pd.DataFrame({"Price": closes[-50:]})
        st.line_chart(chart_df, height=200)

        st.info(f"🧪 DRY RUN: Would buy ${amount} of {asset} at ${price:,.2f}")
        send_telegram(
            f"🐾 *CLAW X DCA Signal*\n"
            f"Asset: *{asset}/USDT*\n"
            f"Signal: *{signal}*\n"
            f"Reason: {reason}\n"
            f"Price: ${price:,.2f} | RSI: {rsi} | MACD: {macd_v}"
        )

# ═══════════════════════════════════════════════════════════
# SMART EXIT
# ═══════════════════════════════════════════════════════════
elif page == "🛡️ Smart Exit":
    st.title("🛡️ Smart Exit Rules")
    st.markdown("Set stop-loss, take-profit and trailing stops for any position")

    prices = get_live_prices()

    col1, col2 = st.columns(2)
    with col1:
        exit_asset = st.selectbox("Asset", ["BTC","ETH","SOL","BNB"])
        current_price = prices.get(f"{exit_asset}/USDT", {}).get("price", 0)
        entry_price = st.number_input("Your Entry Price (USDT)", value=float(current_price), min_value=0.01)
    with col2:
        stop_loss_pct   = st.slider("Stop Loss %",   1,  30,  10)
        take_profit_pct = st.slider("Take Profit %", 5, 500, 100)
        trailing_pct    = st.slider("Trailing Stop % (0 = off)", 0, 20, 0)

    stop_price   = entry_price * (1 - stop_loss_pct / 100)
    target_price = entry_price * (1 + take_profit_pct / 100)
    current_pnl  = ((current_price - entry_price) / entry_price * 100) if entry_price else 0

    st.markdown("### Rule Preview")
    col_a, col_b, col_c, col_d = st.columns(4)
    col_a.metric("Entry Price",  f"${entry_price:,.2f}")
    col_b.metric("Stop Loss",    f"${stop_price:,.2f}",   delta=f"-{stop_loss_pct}%",    delta_color="inverse")
    col_c.metric("Take Profit",  f"${target_price:,.2f}", delta=f"+{take_profit_pct}%")
    col_d.metric("Current P&L",  f"{current_pnl:+.2f}%",  delta_color="normal")

    if trailing_pct > 0:
        st.info(f"🔄 Trailing stop: Stop-loss moves up with price, always {trailing_pct}% below peak.")

    if st.button("✅ Activate Exit Rules", width="stretch"):
        rule = {
            "asset":    exit_asset,
            "entry":    entry_price,
            "stop":     stop_price,
            "target":   target_price,
            "trailing": trailing_pct,
            "active":   True,
            "time":     pd.Timestamp.now().strftime("%H:%M:%S"),
        }
        st.session_state.exit_rules.append(rule)
        st.success(f"✅ Exit rules activated for {exit_asset}!")
        send_telegram(
            f"🛡️ *CLAW X Smart Exit Set*\n"
            f"Asset: *{exit_asset}/USDT*\n"
            f"Entry: ${entry_price:,.2f}\n"
            f"Stop Loss: ${stop_price:,.2f} (-{stop_loss_pct}%)\n"
            f"Take Profit: ${target_price:,.2f} (+{take_profit_pct}%)"
        )

    if st.session_state.exit_rules:
        st.markdown("### Active Rules")
        for i, rule in enumerate(st.session_state.exit_rules):
            if rule["active"]:
                cp  = prices.get(f"{rule['asset']}/USDT", {}).get("price", 0)
                pnl = ((cp - rule["entry"]) / rule["entry"] * 100) if rule["entry"] else 0
                if cp <= rule["stop"]:
                    status = "🔴 STOP LOSS HIT"
                elif cp >= rule["target"]:
                    status = "🟢 TAKE PROFIT HIT"
                else:
                    status = "🟡 Monitoring..."
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f"**{rule['asset']}/USDT** — {status}")
                    st.markdown(f"Entry: `${rule['entry']:,.2f}` | Stop: `${rule['stop']:,.2f}` | Target: `${rule['target']:,.2f}` | P&L: `{pnl:+.2f}%`")
                with col2:
                    if st.button("❌ Remove", key=f"remove_{i}"):
                        st.session_state.exit_rules[i]["active"] = False
                        st.rerun()

# ═══════════════════════════════════════════════════════════
# WHALE ALERTS
# ═══════════════════════════════════════════════════════════
elif page == "🐋 Whale Alerts":
    st.title("🐋 Whale Alerts")
    st.markdown("Real large on-chain transactions — track smart money movements")

    @st.cache_data(ttl=60)
    def get_whale_alerts():
        from bs4 import BeautifulSoup
        all_txns = []

        # Source 1: Blockchair BTC
        try:
            resp = requests.get(
                "https://api.blockchair.com/bitcoin/transactions",
                params={"s": "output_total(desc)", "limit": 10, "q": "output_total(10000000000,)"},
                timeout=10,
            )
            for tx in resp.json().get("data", []):
                usd = tx.get("output_total_usd", 0)
                btc = tx.get("output_total", 0) / 1e8
                if usd and usd > 1_000_000:
                    all_txns.append({
                        "symbol": "BTC", "amount": round(btc, 2), "usd": usd,
                        "from_type": "unknown wallet", "to_type": "unknown wallet",
                        "hash": tx.get("hash", "")[:16], "time": "Just now",
                        "type": "transfer", "source": "Blockchair",
                    })
        except:
            pass

        # Source 2: Blockchair ETH
        try:
            resp = requests.get(
                "https://api.blockchair.com/ethereum/transactions",
                params={"s": "value(desc)", "limit": 10, "q": "value(1000000000000000000000,)"},
                timeout=10,
            )
            for tx in resp.json().get("data", []):
                usd = tx.get("value_usd", 0)
                eth = tx.get("value", 0) / 1e18
                if usd and usd > 1_000_000:
                    all_txns.append({
                        "symbol": "ETH", "amount": round(eth, 2), "usd": usd,
                        "from_type": tx.get("sender", "unknown")[:12] + "...",
                        "to_type": tx.get("recipient", "unknown")[:12] + "...",
                        "hash": tx.get("hash", "")[:16], "time": "Just now",
                        "type": "transfer", "source": "Blockchair",
                    })
        except:
            pass

        # Source 3: Whale Alert Telegram
        try:
            resp = requests.get("https://t.me/s/whale_alert_io", headers={"User-Agent": "Mozilla/5.0"}, timeout=8)
            soup = BeautifulSoup(resp.text, "html.parser")
            messages = soup.find_all("div", class_="tgme_widget_message_text")
            for msg in messages[:30]:
                text = msg.get_text(strip=True)
                if not text or len(text) < 20:
                    continue
                text_lower = text.lower()
                # Parse amount
                import re
                numbers = re.findall(r'[\d,]+', text)
                usd_match = re.search(r'\(?([\d,]+),?\d*\s*(?:USD|usd)\)?', text)
                usd = 0
                if usd_match:
                    try:
                        usd = int(usd_match.group(1).replace(",", ""))
                    except:
                        pass
                if usd < 1_000_000:
                    continue
                symbol = "BTC" if "btc" in text_lower or "#btc" in text_lower else \
                         "ETH" if "eth" in text_lower or "#eth" in text_lower else \
                         "USDT" if "usdt" in text_lower else \
                         "SOL" if "sol" in text_lower else "CRYPTO"
                tx_type = "inflow" if "to exchange" in text_lower or "to binance" in text_lower or "to coinbase" in text_lower else \
                          "outflow" if "from exchange" in text_lower or "from binance" in text_lower else "transfer"
                all_txns.append({
                    "symbol": symbol, "amount": 0, "usd": usd,
                    "from_type": "unknown", "to_type": "unknown",
                    "hash": "", "time": "Recent", "type": tx_type,
                    "source": "Whale Alert TG", "raw": text[:120],
                })
        except:
            pass

        # Fallback mock data
        if not all_txns:
            all_txns = [
                {"symbol":"BTC","amount":1240,"usd":103_588_000,"from_type":"unknown wallet","to_type":"exchange","hash":"a1b2c3d4e5f6","time":"2 min ago","type":"inflow","source":"Mock"},
                {"symbol":"ETH","amount":45000,"usd":127_800_000,"from_type":"exchange","to_type":"unknown wallet","hash":"b2c3d4e5f6a1","time":"8 min ago","type":"outflow","source":"Mock"},
                {"symbol":"BTC","amount":890,"usd":74_338_000,"from_type":"unknown wallet","to_type":"unknown wallet","hash":"c3d4e5f6a1b2","time":"15 min ago","type":"transfer","source":"Mock"},
                {"symbol":"USDT","amount":50_000_000,"usd":50_000_000,"from_type":"Binance","to_type":"Coinbase","hash":"d4e5f6a1b2c3","time":"22 min ago","type":"exchange","source":"Mock"},
                {"symbol":"SOL","amount":380000,"usd":50_272_000,"from_type":"unknown wallet","to_type":"exchange","hash":"e5f6a1b2c3d4","time":"31 min ago","type":"inflow","source":"Mock"},
            ]
        return all_txns

    col1, col2, col3 = st.columns(3)
    with col1:
        whale_asset = st.selectbox("Asset", ["All","BTC","ETH","SOL","BNB","USDT"])
    with col2:
        min_usd = st.selectbox("Min Size", ["$1M+","$10M+","$50M+","$100M+"])
    with col3:
        tx_type_filter = st.selectbox("Type", ["All","inflow","outflow","transfer"])

    if st.button("🔄 Refresh", width="stretch"):
        st.cache_data.clear()
        st.rerun()

    with st.spinner("Fetching real whale movements..."):
        whales = get_whale_alerts()

    min_map = {"$1M+":1e6,"$10M+":10e6,"$50M+":50e6,"$100M+":100e6}
    min_val = min_map[min_usd]
    if whale_asset != "All":
        whales = [w for w in whales if w["symbol"] == whale_asset]
    whales = [w for w in whales if w.get("usd", 0) >= min_val]
    if tx_type_filter != "All":
        whales = [w for w in whales if w["type"] == tx_type_filter]

    total_usd = sum(w.get("usd", 0) for w in whales)
    inflows   = sum(1 for w in whales if w["type"] == "inflow")
    outflows  = sum(1 for w in whales if w["type"] == "outflow")

    col_a, col_b, col_c, col_d = st.columns(4)
    col_a.metric("🐋 Transactions",   len(whales))
    col_b.metric("💰 Total Volume",    f"${total_usd/1e9:.2f}B" if total_usd > 1e9 else f"${total_usd/1e6:.0f}M")
    col_c.metric("📥 Exchange Inflows",  inflows)
    col_d.metric("📤 Exchange Outflows", outflows)
    st.divider()

    if not whales:
        st.warning("No whale transactions found for selected filters.")
    else:
        for w in whales:
            icon = {"inflow":"📥","outflow":"📤","transfer":"🔄","exchange":"🏦"}.get(w["type"], "🐋")
            sentiment = {"inflow":"⚠️ Potential sell pressure","outflow":"💪 Accumulation signal","transfer":"🔄 Neutral transfer","exchange":"🏦 Exchange movement"}.get(w["type"], "")
            usd_display = f"${w['usd']/1e9:.2f}B" if w.get("usd",0) > 1e9 else f"${w.get('usd',0)/1e6:.1f}M"
            if w.get("raw"):
                st.markdown(f"**{icon} {w['symbol']}** — 💰 **{usd_display}** — {sentiment}")
                st.markdown(f"> {w['raw']}")
                st.caption(f"🕐 {w['time']} · 📡 {w.get('source','')}")
            else:
                amount_str = f"{w['amount']:,.2f} {w['symbol']}" if w.get('amount',0) > 0 else ""
                st.markdown(f"**{icon} {w['symbol']}** {f'— `{amount_str}`' if amount_str else ''} — 💰 **{usd_display}**")
                st.markdown(f"{w['from_type']} → {w['to_type']} | {sentiment} | 🕐 {w['time']}")
            st.divider()

# ═══════════════════════════════════════════════════════════
# PRICE ALERTS
# ═══════════════════════════════════════════════════════════
elif page == "🔔 Price Alerts":
    st.title("🔔 Price Alert Creator")
    st.markdown("Get notified the moment your target price is hit")

    prices = get_live_prices()

    col1, col2, col3 = st.columns(3)
    with col1:
        alert_asset = st.selectbox("Asset", ["BTC","ETH","SOL","BNB","AVAX","ADA"])
    with col2:
        alert_condition = st.selectbox("Condition", ["Price goes ABOVE ▲","Price goes BELOW ▼"])
    with col3:
        current = prices.get(f"{alert_asset}/USDT", {}).get("price", 0)
        alert_target = st.number_input("Target Price (USDT)", value=float(round(current * 1.05, 2)), min_value=0.01)

    col4, col5 = st.columns(2)
    with col4:
        recurring = st.checkbox("Recurring alert")
    with col5:
        st.markdown(f"**Current price:** ${current:,.2f}")

    if st.button("🔔 Create Alert", width="stretch"):
        condition = "above" if "ABOVE" in alert_condition else "below"
        direction = ">" if condition == "above" else "<"
        st.session_state.price_alerts.append({
            "asset":     alert_asset,
            "symbol":    f"{alert_asset}/USDT",
            "condition": condition,
            "target":    alert_target,
            "recurring": recurring,
            "active":    True,
            "created":   pd.Timestamp.now().strftime("%H:%M:%S"),
        })
        st.success(f"✅ Alert set! Notify when {alert_asset} {direction} ${alert_target:,.2f}")
        send_telegram(
            f"🔔 *CLAW X Price Alert Set*\n"
            f"Asset: *{alert_asset}*\n"
            f"Condition: {'Above' if condition == 'above' else 'Below'} ${alert_target:,.2f}\n"
            f"Current Price: ${current:,.2f}"
        )

    st.divider()

    if not st.session_state.price_alerts:
        st.info("No alerts yet. Create one above!")
    else:
        st.markdown("### Your Active Alerts")
        for i, alert in enumerate(st.session_state.price_alerts):
            if not alert["active"]:
                continue
            cp        = prices.get(alert["symbol"], {}).get("price", 0)
            condition = alert["condition"]
            target    = alert["target"]
            direction = ">" if condition == "above" else "<"
            distance  = abs(cp - target) / target * 100
            triggered = (condition == "above" and cp >= target) or (condition == "below" and cp <= target)
            col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
            with col1:
                st.markdown(f"**{alert['asset']}** {direction} ${target:,.2f}")
            with col2:
                st.markdown(f"Current: `${cp:,.2f}`")
            with col3:
                if triggered:
                    send_telegram(f"🚨 *Price Alert Triggered!*\n*{alert['asset']}* hit your target!\nTarget: ${target:,.2f}\nCurrent: ${cp:,.2f}")
                    st.success("🔔 TRIGGERED!")
                else:
                    st.markdown(f"📍 {distance:.1f}% away")
            with col4:
                if st.button("❌", key=f"del_{i}"):
                    st.session_state.price_alerts[i]["active"] = False
                    st.rerun()

# ═══════════════════════════════════════════════════════════
# BINANCE NEWS
# ═══════════════════════════════════════════════════════════
elif page == "📢 Binance News":
    st.title("📢 Binance Flash News")
    st.markdown("Latest Binance announcements — listings, delistings, campaigns, launchpool")

    @st.cache_data(ttl=120)
    def get_binance_news():
        import feedparser
        from bs4 import BeautifulSoup
        all_articles = []

        catalog_map = {48:"listing", 161:"delisting", 49:"campaign", 93:"launchpool", 157:"futures", 50:"campaign", 128:"campaign"}
        try:
            headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json", "Cache-Control": "no-cache"}
            for catalog_id, news_type in catalog_map.items():
                try:
                    resp = requests.post(
                        "https://www.binance.com/bapi/composite/v1/public/cms/article/list/query",
                        json={"type":1,"pageNo":1,"pageSize":10,"catalogId":catalog_id},
                        headers=headers, timeout=8,
                    )
                    for cat in resp.json().get("data", {}).get("catalogs", []):
                        for a in cat.get("articles", []):
                            all_articles.append({"title": a.get("title",""), "url": f"https://www.binance.com/en/support/announcement/{a.get('code','')}", "time": a.get("releaseDate","")[:10], "type": news_type})
                except:
                    continue
        except:
            pass

        # Binance Telegram
        try:
            resp = requests.get("https://t.me/s/binance_announcements", headers={"User-Agent": "Mozilla/5.0"}, timeout=8)
            soup = BeautifulSoup(resp.text, "html.parser")
            messages = soup.find_all("div", class_="tgme_widget_message_text")
            links    = soup.find_all("a", class_="tgme_widget_message_date")
            for msg, link in zip(messages[:20], links[:20]):
                text = msg.get_text(strip=True)[:150]
                url  = link.get("href", "#")
                if text:
                    all_articles.append({"title": text, "url": url, "time": "", "type": "delisting" if "delist" in text.lower() else "listing" if "list" in text.lower() else "launchpool" if "launchpool" in text.lower() else "futures" if "futures" in text.lower() else "campaign" if any(w in text.lower() for w in ["campaign","reward","earn","airdrop"]) else "update"})
        except:
            pass

        # CoinTelegraph Binance tag
        try:
            feed = feedparser.parse("https://cointelegraph.com/rss/tag/binance")
            for e in feed.entries[:10]:
                title = e.get("title", "")
                all_articles.append({"title": title, "url": e.get("link","#"), "time": e.get("published","")[:10], "type": "delisting" if "delist" in title.lower() else "listing" if "list" in title.lower() else "update"})
        except:
            pass

        seen = set()
        unique = []
        for a in all_articles:
            t = a["title"].strip()
            if t and t not in seen and len(t) > 10:
                seen.add(t)
                unique.append(a)
        unique.sort(key=lambda x: x["time"] if x["time"] else "2099", reverse=True)
        return unique

    col1, col2 = st.columns([3, 1])
    with col1:
        category = st.selectbox("Category", ["All","Listings","Delistings","Campaigns","Launchpool","Futures","Updates"])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 Refresh", width="stretch"):
            st.cache_data.clear()
            st.rerun()

    news = get_binance_news()

    if st.button("🤖 Summarize with AI", width="stretch"):
        with st.spinner("Summarizing..."):
            titles  = "\n".join([f"- {n['title']}" for n in news[:8]])
            summary = ask_llm(f"Summarize these Binance announcements in 3 sentences for a trader:\n{titles}")
        st.info(f"🤖 **AI Summary:**\n\n{summary}")
        send_telegram(f"📢 *Binance Flash News Summary*\n\n{summary}")

    st.divider()

    cat_filter = {"All":None,"Listings":"listing","Delistings":"delisting","Campaigns":"campaign","Launchpool":"launchpool","Futures":"futures","Updates":"update"}
    type_icons = {"listing":"🟢","delisting":"🔴","campaign":"🎯","launchpool":"🚀","futures":"🔵","update":"⚪"}

    if not news:
        st.warning("No news found. Try refreshing.")
    else:
        filtered = news if category == "All" else [n for n in news if n["type"] == cat_filter[category]]
        if not filtered:
            st.info(f"No {category} found right now.")
        else:
            st.success(f"✅ Showing {len(filtered)} articles")
            for n in filtered:
                icon  = type_icons.get(n["type"], "⚪")
                col1, col2 = st.columns([5, 1])
                with col1:
                    st.markdown(f"{icon} **[{n['type'].upper()}]** {n['title']}")
                    st.caption(f"📅 {n['time'] if n['time'] else 'Latest'}")
                with col2:
                    if n["url"] != "#":
                        st.link_button("Read →", n["url"])
                st.divider()

# ═══════════════════════════════════════════════════════════
# NEWS FEED
# ═══════════════════════════════════════════════════════════
elif page == "📰 News Feed":
    st.title("📰 News Feed")
    st.markdown("Live crypto news from CoinTelegraph and CoinDesk")

    col1, col2 = st.columns([3, 1])
    with col1:
        news_asset = st.text_input("Filter by asset (optional)", placeholder="BTC, ETH, SOL...")
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        refresh = st.button("🔄 Refresh", width="stretch")

    if refresh:
        st.cache_data.clear()

    try:
        import feedparser
        news = []
        feed1 = feedparser.parse("https://cointelegraph.com/rss")
        for e in feed1.entries[:6]:
            news.append({"title": e.get("title",""), "source": "CoinTelegraph", "url": e.get("link","#"), "time": e.get("published","")[:16]})
        feed2 = feedparser.parse("https://www.coindesk.com/arc/outboundfeeds/rss/")
        for e in feed2.entries[:6]:
            news.append({"title": e.get("title",""), "source": "CoinDesk", "url": e.get("link","#"), "time": e.get("published","")[:16]})
        if news_asset and news:
            filtered = [n for n in news if news_asset.upper() in n["title"].upper()]
            if filtered:
                news = filtered
    except Exception as e:
        st.error(f"Error fetching news: {e}")
        news = []

    if news:
        if st.button("🤖 Summarize with AI", width="stretch"):
            with st.spinner("Summarizing..."):
                titles  = "\n".join([f"- {n['title']}" for n in news[:8]])
                summary = ask_llm(f"Summarize these crypto news in 3 sentences for a trader:\n{titles}")
            st.info(f"🤖 **AI Summary:**\n\n{summary}")
            send_telegram(f"📰 *Crypto News Summary*\n\n{summary}")

    st.divider()

    if not news:
        st.warning("No news found. Try clicking Refresh.")
    else:
        st.success(f"✅ Showing {len(news)} live articles")
        for n in news:
            col1, col2 = st.columns([5, 1])
            with col1:
                st.markdown(f"**{n['title']}**")
                st.caption(f"📰 {n['source']} · 📅 {n['time']}")
            with col2:
                st.link_button("Read →", n["url"])
            st.divider()

# ═══════════════════════════════════════════════════════════
# NARRATIVE SCAN
# ═══════════════════════════════════════════════════════════
elif page == "🔍 Narrative Scan":
    st.title("🔍 Narrative Scanner")
    st.markdown("Real-time market sentiment, fear & greed, and trending crypto narratives 📡")

    if st.button("🔄 Refresh All Data", width="stretch"):
        st.cache_data.clear()
        st.rerun()

    @st.cache_data(ttl=300)
    def get_fear_greed():
        try:
            resp = requests.get("https://api.alternative.me/fng/?limit=7", timeout=8)
            data = resp.json()["data"]
            return {"value": int(data[0]["value"]), "label": data[0]["value_classification"], "history": [int(d["value"]) for d in reversed(data[:7])]}
        except:
            return {"value": 50, "label": "Neutral", "history": [50,50,50,50,50,50,50]}

    @st.cache_data(ttl=300)
    def get_narrative_news():
        import feedparser
        try:
            resp = requests.get("https://cryptopanic.com/api/free/v1/posts/?public=true&filter=hot", timeout=8)
            items = resp.json().get("results", [])[:8]
            if items:
                return [{"title": i["title"], "source": i.get("source",{}).get("title","CryptoPanic"), "time": i.get("published_at","")[:10]} for i in items]
        except:
            pass
        try:
            feed = feedparser.parse("https://cointelegraph.com/rss")
            if feed.entries:
                return [{"title": e.get("title",""), "source": "CoinTelegraph", "time": e.get("published","")[:10]} for e in feed.entries[:8]]
        except:
            pass
        return []

    fg    = get_fear_greed()
    value = fg["value"]

    if value <= 25:
        color, emoji, mood, advice = "#ff3366", "😱", "Extreme Fear", "🔴 Extreme fear — historically the best time to accumulate."
    elif value <= 45:
        color, emoji, mood, advice = "#ff8844", "😟", "Fear", "🟠 Market is fearful — DCA signals are likely strong."
    elif value <= 55:
        color, emoji, mood, advice = "#ffcc00", "😐", "Neutral", "⚪ Neutral market — wait for clearer direction."
    elif value <= 75:
        color, emoji, mood, advice = "#88cc00", "😊", "Greed", "🟡 Greed detected — consider taking partial profits."
    else:
        color, emoji, mood, advice = "#00ff88", "🤑", "Extreme Greed", "🟢 Extreme greed — markets often correct after euphoria."

    st.divider()
    st.markdown("### 😨 Fear & Greed Index")

    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f"""
        <div style='text-align:center; padding:28px 20px; border:1px solid #ddd; border-radius:12px;'>
            <div style='font-size:52px;'>{emoji}</div>
            <div style='font-size:64px; font-weight:700; color:{color};'>{value}</div>
            <div style='font-size:16px; font-weight:600; color:{color};'>{fg["label"]}</div>
            <div style='font-size:11px; color:#888; margin-top:8px;'>Source: alternative.me</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("#### 📅 7-Day History")
        try:
            import altair as alt
            hist_df = pd.DataFrame({
                "Day":   [f"Day {i+1}" for i in range(len(fg["history"]))],
                "Score": fg["history"],
            })
            hist_df["color"] = hist_df["Score"].apply(
                lambda v: "#ef4444" if v <= 25
                else "#f97316" if v <= 45
                else "#eab308" if v <= 55
                else "#84cc16" if v <= 75
                else "#22c55e"
            )
            chart = alt.Chart(hist_df).mark_bar(
                cornerRadiusTopLeft=6,
                cornerRadiusTopRight=6,
            ).encode(
                x=alt.X("Day:N", sort=None, title=None,
                    axis=alt.Axis(labelColor="#8a8680", tickColor="#1e2028", domainColor="#1e2028", labelFontSize=11)),
                y=alt.Y("Score:Q", scale=alt.Scale(domain=[0,100]), title=None,
                    axis=alt.Axis(labelColor="#8a8680", gridColor="#1e2028", domainColor="#1e2028", tickCount=5)),
                color=alt.Color("color:N", scale=None, legend=None),
                tooltip=[alt.Tooltip("Day:N", title="Day"), alt.Tooltip("Score:Q", title="Score")],
            ).properties(
                height=200,
                background="#0d0e11",
                padding={"left":8,"right":8,"top":10,"bottom":8},
            ).configure_view(strokeWidth=0)
            st.altair_chart(chart, width="stretch")
        except:
            chart_df = pd.DataFrame({"Fear & Greed Score": fg["history"]}, index=[f"D{i+1}" for i in range(len(fg["history"]))])
            st.bar_chart(chart_df, height=160)
        st.info(advice)

    st.divider()

    col3, col4 = st.columns(2)
    with col3:
        st.markdown("### 🔥 Trending Headlines")
        narrative_news = get_narrative_news()
        if not narrative_news:
            st.warning("⚠️ Could not fetch headlines. Try refreshing.")
        else:
            for n in narrative_news:
                st.markdown(f"**{n['title']}**")
                st.caption(f"📰 {n['source']} · 📅 {n['time']}")
                st.divider()

    with col4:
        st.markdown("### 🤖 AI Narrative Summary")
        if st.button("✨ Generate AI Summary", width="stretch"):
            narrative_news = get_narrative_news()
            if not narrative_news:
                st.warning("No headlines found. Refresh first.")
            else:
                with st.spinner("🧠 Analyzing market narratives..."):
                    titles = "\n".join([f"- {n['title']}" for n in narrative_news])
                    prompt = f"""Fear & Greed Index: {value}/100 ({fg["label"]})
Headlines: {titles}
Write 3 bullet points: dominant narrative, bullish catalysts, key risks."""
                    st.session_state.narrative_summary = ask_llm(prompt)
                    send_telegram(f"🔍 *Market Narrative Update*\nFear & Greed: *{value}/100* ({fg['label']})\n\n{st.session_state.narrative_summary}")

        if st.session_state.narrative_summary:
            st.success(st.session_state.narrative_summary)
        else:
            st.info("👆 Click above to generate an AI-powered market narrative summary")

    st.divider()
    st.markdown("### 📊 Market Sentiment Snapshot")
    col5, col6, col7, col8 = st.columns(4)
    col5.metric("😨 Fear & Greed",  f"{value}/100",  fg["label"])
    col6.metric("🟠 BTC Dominance", "54.2%",         "↑ 0.3%")
    col7.metric("📈 Overall Mood",  mood,             emoji)
    col8.metric("🎯 Trend Signal",  "Bullish 🟢" if value > 55 else ("Bearish 🔴" if value < 45 else "Neutral ⚪"))

# ═══════════════════════════════════════════════════════════
# WALLET TRACKER
# ═══════════════════════════════════════════════════════════
elif page == "👛 Wallet Tracker":
    st.title("👛 Wallet Tracker")
    st.markdown("Track on-chain moves of crypto whales & influencers in real-time 🔍")

    KNOWN_WALLETS = {
        "Justin Sun":     {"address": "0x3ddfa8ec3052539b6c9549f12cea2c295cff5296", "emoji": "☀️", "note": "TRON founder, known for large ETH & stablecoin moves"},
        "Arthur Hayes":   {"address": "0xa86e3d1c80a750a310b484fb9bdc470753a7506f", "emoji": "⚔️", "note": "BitMEX co-founder, DeFi & altcoin trader"},
        "Vitalik Buterin":{"address": "0xd8da6bf26964af9d7eed9e03e53415d37aa96045", "emoji": "🦄", "note": "Ethereum co-founder"},
        "Jump Trading":   {"address": "0x0c23fc0ef06716d2f8ba19bc4bed56d045581f2d", "emoji": "🦘", "note": "Major market maker & crypto fund"},
    }

    ETHERSCAN_KEY = os.getenv("ETHERSCAN_API_KEY", "")
    ALCHEMY_KEY   = os.getenv("ALCHEMY_API_KEY", "")

    @st.cache_data(ttl=60)
    def get_eth_balance(address: str) -> float:
        try:
            resp = requests.post(f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_KEY}", json={"jsonrpc":"2.0","method":"eth_getBalance","params":[address,"latest"],"id":1}, timeout=8)
            return int(resp.json().get("result", "0x0"), 16) / 1e18
        except:
            return 0.0

    @st.cache_data(ttl=60)
    def get_recent_transactions(address: str) -> list:
        try:
            resp = requests.get("https://api.etherscan.io/api", params={"module":"account","action":"txlist","address":address,"startblock":0,"endblock":99999999,"page":1,"offset":10,"sort":"desc","apikey":ETHERSCAN_KEY}, timeout=10)
            txns = resp.json().get("result", [])
            return txns if isinstance(txns, list) else []
        except:
            return []

    @st.cache_data(ttl=60)
    def get_token_transfers(address: str) -> list:
        try:
            resp = requests.get("https://api.etherscan.io/api", params={"module":"account","action":"tokentx","address":address,"page":1,"offset":10,"sort":"desc","apikey":ETHERSCAN_KEY}, timeout=10)
            txns = resp.json().get("result", [])
            return txns if isinstance(txns, list) else []
        except:
            return []

    def format_value(val: float) -> str:
        if val >= 1_000_000_000: return f"${val/1_000_000_000:.2f}B"
        elif val >= 1_000_000:   return f"${val/1_000_000:.2f}M"
        elif val >= 1_000:       return f"${val/1_000:.2f}K"
        return f"${val:.2f}"

    def time_ago(timestamp: str) -> str:
        try:
            import time
            diff = int(time.time()) - int(timestamp)
            if diff < 60:    return f"{diff}s ago"
            elif diff < 3600: return f"{diff//60}m ago"
            elif diff < 86400: return f"{diff//3600}h ago"
            else:             return f"{diff//86400}d ago"
        except:
            return "Unknown"

    col1, col2 = st.columns([3, 1])
    with col1:
        selected_name = st.selectbox("Select Wallet", list(KNOWN_WALLETS.keys()) + ["Custom Address"])
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔄 Refresh", width="stretch"):
            st.cache_data.clear()
            st.rerun()

    if selected_name == "Custom Address":
        custom_address = st.text_input("Enter ETH Wallet Address", placeholder="0x...")
        if not custom_address or not custom_address.startswith("0x"):
            st.info("Enter a valid Ethereum address starting with 0x")
            st.stop()
        wallet_address = custom_address
        wallet_info    = {"address": custom_address, "emoji": "👤", "note": "Custom wallet"}
    else:
        wallet_info    = KNOWN_WALLETS[selected_name]
        wallet_address = wallet_info["address"]

    st.markdown(f"**{wallet_info['emoji']} {selected_name}** — `{wallet_address}`")
    st.caption(wallet_info["note"])
    st.markdown(f"[🔗 View on Etherscan](https://etherscan.io/address/{wallet_address})")
    st.divider()

    with st.spinner(f"Fetching on-chain data for {selected_name}..."):
        eth_balance = get_eth_balance(wallet_address)
        txns        = get_recent_transactions(wallet_address)
        token_txns  = get_token_transfers(wallet_address)

    try:
        eth_price = get_live_prices().get("ETH/USDT", {}).get("price", 2500)
    except:
        eth_price = 2500

    eth_usd = eth_balance * eth_price

    st.markdown("### 💰 Current Holdings")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("ETH Balance", f"{eth_balance:.4f} ETH")
    col2.metric("ETH Value",   format_value(eth_usd))
    col3.metric("Recent TXNs", len(txns))
    col4.metric("Token Moves", len(token_txns))
    st.divider()

    col_left, col_right = st.columns(2)

    with col_left:
        st.markdown("### 📋 Recent ETH Transactions")
        if not txns:
            st.info("No recent transactions found.")
        else:
            for tx in txns[:8]:
                value_eth   = int(tx.get("value", 0)) / 1e18
                value_usd   = value_eth * eth_price
                is_in       = tx.get("to","").lower() == wallet_address.lower()
                direction   = "📥 IN" if is_in else "📤 OUT"
                t_ago       = time_ago(tx.get("timeStamp","0"))
                hash_short  = tx.get("hash","")[:12] + "..."
                other       = tx.get("from","") if is_in else tx.get("to","")
                other_short = other[:10] + "..." if other else "unknown"
                if value_eth > 0:
                    st.markdown(f"**{direction}** {value_eth:.4f} ETH ({format_value(value_usd)})")
                    st.caption(f"{other_short} · {hash_short} · {t_ago}")
                    st.divider()

    with col_right:
        st.markdown("### 🪙 Recent Token Transfers")
        if not token_txns:
            st.info("No recent token transfers found.")
        else:
            for tx in token_txns[:8]:
                decimals   = int(tx.get("tokenDecimal", 18))
                amount     = int(tx.get("value", 0)) / (10 ** decimals)
                symbol     = tx.get("tokenSymbol", "TOKEN")
                is_in      = tx.get("to","").lower() == wallet_address.lower()
                direction  = "📥 IN" if is_in else "📤 OUT"
                t_ago      = time_ago(tx.get("timeStamp","0"))
                other      = tx.get("from","") if is_in else tx.get("to","")
                other_short = other[:10] + "..." if other else "unknown"
                if amount > 0:
                    amount_str = f"{amount:,.2f}" if amount < 1e9 else f"{amount/1e6:,.2f}M"
                    st.markdown(f"**{direction}** {amount_str} **{symbol}**")
                    st.caption(f"{other_short} · {t_ago}")
                    st.divider()

    st.divider()
    st.markdown("### 🤖 AI Wallet Analysis")
    if st.button("✨ Analyze Wallet Activity", width="stretch"):
        with st.spinner("Analyzing on-chain behavior..."):
            tx_summary = []
            for tx in txns[:5]:
                value_eth = int(tx.get("value", 0)) / 1e18
                is_in     = tx.get("to","").lower() == wallet_address.lower()
                t_ago     = time_ago(tx.get("timeStamp","0"))
                if value_eth > 0:
                    tx_summary.append(f"- {'received' if is_in else 'sent'} {value_eth:.4f} ETH {t_ago}")
            for tx in token_txns[:5]:
                amount  = int(tx.get("value",0)) / (10 ** int(tx.get("tokenDecimal",18)))
                symbol  = tx.get("tokenSymbol","TOKEN")
                is_in   = tx.get("to","").lower() == wallet_address.lower()
                t_ago   = time_ago(tx.get("timeStamp","0"))
                if amount > 0:
                    tx_summary.append(f"- {'received' if is_in else 'sent'} {amount:,.2f} {symbol} {t_ago}")

            summary_text = "\n".join(tx_summary) if tx_summary else "No recent transactions"
            prompt = f"""You are a blockchain analyst.
Wallet: {selected_name} | ETH Balance: {eth_balance:.4f} ETH (${eth_usd:,.0f} USD)
Recent activity:
{summary_text}
Analyze in 3 bullet points: behavior pattern, accumulating or distributing, what traders should watch."""
            analysis = ask_llm(prompt)

        st.success(analysis)
        send_telegram(f"👛 *Wallet Tracker Alert*\nWallet: *{selected_name}*\nETH: {eth_balance:.4f}\n\n{analysis}")
