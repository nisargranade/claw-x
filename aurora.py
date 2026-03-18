# aurora.py — CLAW X Gold Theme
# Add to app.py after st.set_page_config():
#   from aurora import skin
#   skin()

import streamlit as st

def skin():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --amber:       #f0a500;
    --amber-dim:   #b87c00;
    --amber-glow:  rgba(240,165,0,0.12);
    --amber-faint: rgba(240,165,0,0.06);
    --bg:          #0d0e11;
    --bg-card:     #12141a;
    --bg-input:    #161820;
    --bg-hover:    #1c1e26;
    --border:      #1e2028;
    --border-lit:  #2e3040;
    --text-hi:     #f0ece4;
    --text-md:     #8a8680;
    --text-lo:     #3a3830;
    --green:       #22c55e;
    --green-dim:   rgba(34,197,94,0.12);
    --red:         #ef4444;
    --red-dim:     rgba(239,68,68,0.12);
}

html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif !important;
    background: var(--bg) !important;
    color: var(--text-hi) !important;
    font-size: 15px !important;
}
.stApp { background: var(--bg) !important; }
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(240,165,0,0.015) 1px, transparent 1px),
        linear-gradient(90deg, rgba(240,165,0,0.015) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: #0a0b0e !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-md) !important; font-size: 14px !important; }
[data-testid="stSidebar"] h2 {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    font-size: 20px !important;
    color: var(--amber) !important;
}

/* ── SIDEBAR BUTTONS ── */
section[data-testid="stSidebar"] button {
    all: unset !important;
    display: block !important;
    width: 100% !important;
    box-sizing: border-box !important;
    padding: 9px 14px !important;
    margin-bottom: 1px !important;
    border-radius: 6px !important;
    cursor: pointer !important;
    color: var(--text-md) !important;
    font-size: 14px !important;
    font-family: 'Outfit', sans-serif !important;
    transition: all 0.15s !important;
    border-left: 2px solid transparent !important;
}
section[data-testid="stSidebar"] button:hover {
    background: var(--amber-faint) !important;
    border-left-color: var(--amber-dim) !important;
    color: var(--amber) !important;
    padding-left: 18px !important;
}
section[data-testid="stSidebar"] button p {
    color: inherit !important;
    font-size: 14px !important;
    margin: 0 !important;
}

/* ── HEADINGS ── */
h1 {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    font-size: 28px !important;
    color: var(--text-hi) !important;
    border-bottom: 1px solid var(--border) !important;
    padding-bottom: 14px !important;
    margin-bottom: 4px !important;
}
h2 { font-family: 'Outfit', sans-serif !important; font-weight: 600 !important; font-size: 20px !important; color: var(--text-hi) !important; }
h3 { font-family: 'Outfit', sans-serif !important; font-weight: 500 !important; font-size: 16px !important; color: #b0aca4 !important; }

p { color: #c8c4bc !important; font-size: 14px !important; line-height: 1.65 !important; }
strong { color: var(--text-hi) !important; font-weight: 600 !important; }
code {
    font-family: 'JetBrains Mono', monospace !important;
    background: var(--bg-input) !important;
    color: var(--amber) !important;
    padding: 2px 7px !important;
    border-radius: 4px !important;
    font-size: 12px !important;
    border: 1px solid var(--border-lit) !important;
}

/* ── MAIN BUTTONS ── */
.stButton > button {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-lit) !important;
    color: var(--text-hi) !important;
    border-radius: 6px !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 500 !important;
    font-size: 14px !important;
    padding: 9px 20px !important;
    transition: all 0.15s !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    background: var(--amber-glow) !important;
    border-color: var(--amber) !important;
    color: var(--amber) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 20px rgba(240,165,0,0.1) !important;
}

/* ── ALL INPUTS ── */
input, textarea,
div[data-baseweb="input"] input,
.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background: var(--bg-input) !important;
    color: var(--text-hi) !important;
    border: 1px solid var(--border-lit) !important;
    border-radius: 6px !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 14px !important;
    caret-color: var(--amber) !important;
}
input::placeholder, textarea::placeholder { color: var(--text-lo) !important; }
input:focus, textarea:focus {
    border-color: var(--amber-dim) !important;
    box-shadow: 0 0 0 3px rgba(240,165,0,0.08) !important;
    outline: none !important;
}

/* ── CHAT INPUT ── */
[data-testid="stChatInput"],
[data-testid="stChatInput"] *,
[data-testid="stChatInput"] > div,
[data-testid="stChatInput"] > div > div,
[data-testid="stChatInput"] > div > div > div,
[data-testid="stChatInput"] textarea,
[data-testid="stChatInput"] div[data-baseweb="textarea"],
[data-testid="stChatInput"] div[data-baseweb="base-input"] {
    background: var(--bg-input) !important;
    background-color: var(--bg-input) !important;
    color: var(--text-hi) !important;
    caret-color: var(--amber) !important;
    border-color: var(--border-lit) !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: var(--text-lo) !important; }

/* ── SELECTBOX ── */
div[data-baseweb="select"] > div { background: var(--bg-input) !important; border: 1px solid var(--border-lit) !important; border-radius: 6px !important; }
div[data-baseweb="select"] span, div[data-baseweb="select"] div { background: var(--bg-input) !important; color: var(--text-hi) !important; font-size: 14px !important; }
li[role="option"] { background: var(--bg-input) !important; color: #b0aca4 !important; font-size: 14px !important; padding: 8px 14px !important; }
li[role="option"]:hover, li[aria-selected="true"] { background: var(--amber-glow) !important; color: var(--amber) !important; }

/* ── NUMBER INPUT ── */
div[data-testid="stNumberInput"] > div { background: var(--bg-input) !important; border: 1px solid var(--border-lit) !important; border-radius: 6px !important; }
div[data-testid="stNumberInput"] button { background: var(--bg-hover) !important; color: var(--text-md) !important; border: none !important; }
div[data-testid="stNumberInput"] button:hover { color: var(--amber) !important; background: var(--amber-faint) !important; }

/* ── SLIDER ── */
div[data-testid="stSlider"] div[role="slider"] { background: var(--amber) !important; border: 2px solid var(--bg) !important; box-shadow: 0 0 8px rgba(240,165,0,0.4) !important; }
div[data-testid="stSlider"] > div > div > div > div { background: var(--amber) !important; }
div[data-testid="stSlider"] p { color: var(--text-md) !important; font-size: 13px !important; font-family: 'JetBrains Mono', monospace !important; }

/* ── METRICS ── */
div[data-testid="stMetric"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    padding: 16px 18px !important;
    position: relative !important;
    overflow: hidden !important;
}
div[data-testid="stMetric"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--amber), transparent);
}
div[data-testid="stMetricLabel"] > div { color: var(--text-md) !important; font-size: 11px !important; font-family: 'JetBrains Mono', monospace !important; text-transform: uppercase !important; letter-spacing: 1.5px !important; }
div[data-testid="stMetricValue"] > div { color: var(--text-hi) !important; font-family: 'JetBrains Mono', monospace !important; font-size: 26px !important; font-weight: 600 !important; }
div[data-testid="stMetricDelta"] > div { font-family: 'JetBrains Mono', monospace !important; font-size: 12px !important; }

/* ── ALERTS ── */
div[data-testid="stAlert"] { border-radius: 6px !important; font-size: 14px !important; padding: 12px 16px !important; background: var(--bg-card) !important; border: 1px solid var(--border-lit) !important; color: #c8c4bc !important; }
.stSuccess { background: var(--green-dim) !important; border-color: rgba(34,197,94,0.3) !important; color: #6ee7a0 !important; }
.stWarning { background: rgba(240,165,0,0.08) !important; border-color: rgba(240,165,0,0.25) !important; color: var(--amber) !important; }
.stError   { background: var(--red-dim) !important; border-color: rgba(239,68,68,0.3) !important; color: #fca5a5 !important; }

/* ── CHAT MESSAGES ── */
[data-testid="stChatMessage"] { background: var(--bg-card) !important; border: 1px solid var(--border) !important; border-radius: 10px !important; margin-bottom: 8px !important; }
[data-testid="stChatMessage"] p { color: #c8c4bc !important; font-size: 14px !important; }

/* ── CHARTS ── */
[data-testid="stArrowVegaLiteChart"] { background: var(--bg-card) !important; border-radius: 8px !important; border: 1px solid var(--border) !important; padding: 8px !important; }

/* ── MARKDOWN ── */
.stMarkdown p { color: #c8c4bc !important; font-size: 14px !important; }
.stMarkdown strong { color: var(--text-hi) !important; }
.stMarkdown a { color: var(--amber) !important; text-decoration: none !important; }

/* ── CHECKBOX ── */
label[data-testid="stCheckbox"] span { color: var(--text-md) !important; font-size: 14px !important; }

/* ── LINK / READ BUTTON ── */
a[data-testid="stLinkButton"] {
    background: #1c1e26 !important;
    border: 1px solid #22c55e !important;
    color: #22c55e !important;
    border-radius: 6px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    font-family: 'Outfit', sans-serif !important;
    transition: all 0.15s !important;
}
a[data-testid="stLinkButton"]:hover { background: rgba(34,197,94,0.1) !important; border-color: #22c55e !important; }
/* ── DIVIDER ── */
hr { border: none !important; border-top: 1px solid var(--border) !important; margin: 20px 0 !important; }

/* ── CAPTION ── */
small, .stCaption { color: var(--text-md) !important; font-size: 12px !important; font-family: 'JetBrains Mono', monospace !important; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border-lit); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--amber-dim); }

::selection { background: rgba(240,165,0,0.2); color: var(--amber); }

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
</style>
""", unsafe_allow_html=True)

