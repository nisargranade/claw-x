NEW_CSS = '''st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');

/* ── BASE ── */
html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif !important;
    background: #0b0e11 !important;
    color: #eaecef !important;
    font-size: 14px !important;
}
.stApp { background: #0b0e11 !important; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: #1e2026 !important;
    border-right: 1px solid #2b2f36 !important;
}

/* ── SIDEBAR ALL TEXT ── */
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] label {
    color: #848e9c !important;
    font-size: 14px !important;
}

/* ── SIDEBAR BUTTONS — SIMPLE AND VISIBLE ── */
section[data-testid="stSidebar"] button {
    all: unset !important;
    display: block !important;
    width: 100% !important;
    padding: 9px 14px !important;
    margin-bottom: 2px !important;
    border-radius: 4px !important;
    cursor: pointer !important;
    color: #848e9c !important;
    font-size: 14px !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    box-sizing: border-box !important;
    transition: background 0.1s !important;
}
section[data-testid="stSidebar"] button:hover {
    background: #2b2f36 !important;
    color: #eaecef !important;
}
section[data-testid="stSidebar"] button p {
    color: inherit !important;
    font-size: 14px !important;
    margin: 0 !important;
}

/* ── HEADINGS ── */
h1 {
    font-weight: 600 !important;
    font-size: 24px !important;
    color: #eaecef !important;
    border-bottom: 1px solid #2b2f36 !important;
    padding-bottom: 12px !important;
    margin-bottom: 8px !important;
}
h2 { font-weight: 600 !important; font-size: 18px !important; color: #eaecef !important; }
h3 { font-weight: 500 !important; font-size: 15px !important; color: #848e9c !important; }

/* ── TEXT ── */
p { color: #848e9c !important; font-size: 14px !important; line-height: 1.6 !important; }
strong { color: #eaecef !important; font-weight: 600 !important; }
code {
    font-family: 'IBM Plex Mono', monospace !important;
    background: #2b2f36 !important;
    color: #f0b90b !important;
    padding: 2px 6px !important;
    border-radius: 3px !important;
    font-size: 12px !important;
}

/* ── MAIN BUTTONS ── */
.stButton > button {
    background: #f0b90b !important;
    border: none !important;
    color: #1e2026 !important;
    border-radius: 4px !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    padding: 8px 18px !important;
    transition: background 0.1s !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    background: #b08b00 !important;
}

/* ── INPUTS ── */
input, textarea,
div[data-baseweb="input"] input,
.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    background: #2b2f36 !important;
    color: #eaecef !important;
    border: 1px solid #363c45 !important;
    border-radius: 4px !important;
    font-size: 14px !important;
    caret-color: #f0b90b !important;
}
input::placeholder, textarea::placeholder { color: #474d57 !important; }
input:focus, textarea:focus {
    border-color: #f0b90b !important;
    outline: none !important;
    box-shadow: none !important;
}

/* ── CHAT INPUT ── */
[data-testid="stChatInput"] > div,
[data-testid="stChatInput"] textarea,
[data-testid="stChatInput"] * {
    background: #2b2f36 !important;
    background-color: #2b2f36 !important;
    color: #eaecef !important;
    caret-color: #f0b90b !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: #474d57 !important; }

/* ── SELECTBOX ── */
div[data-baseweb="select"] > div { background: #2b2f36 !important; border: 1px solid #363c45 !important; border-radius: 4px !important; }
div[data-baseweb="select"] span, div[data-baseweb="select"] div { background: #2b2f36 !important; color: #eaecef !important; }
li[role="option"] { background: #1e2026 !important; color: #848e9c !important; }
li[role="option"]:hover, li[aria-selected="true"] { background: #2b2f36 !important; color: #eaecef !important; }

/* ── NUMBER INPUT ── */
div[data-testid="stNumberInput"] > div { background: #2b2f36 !important; border: 1px solid #363c45 !important; border-radius: 4px !important; }
div[data-testid="stNumberInput"] button { background: #363c45 !important; color: #848e9c !important; border: none !important; }

/* ── SLIDER ── */
div[data-testid="stSlider"] div[role="slider"] { background: #f0b90b !important; border: 2px solid #0b0e11 !important; }
div[data-testid="stSlider"] > div > div > div > div { background: #f0b90b !important; }
div[data-testid="stSlider"] p { color: #848e9c !important; font-size: 13px !important; }

/* ── METRICS ── */
div[data-testid="stMetric"] {
    background: #1e2026 !important;
    border: 1px solid #2b2f36 !important;
    border-radius: 4px !important;
    padding: 16px !important;
}
div[data-testid="stMetricLabel"] > div { color: #848e9c !important; font-size: 11px !important; text-transform: uppercase !important; letter-spacing: 0.5px !important; font-family: 'IBM Plex Mono', monospace !important; }
div[data-testid="stMetricValue"] > div { color: #eaecef !important; font-family: 'IBM Plex Mono', monospace !important; font-size: 22px !important; font-weight: 600 !important; }
div[data-testid="stMetricDelta"] > div { font-family: 'IBM Plex Mono', monospace !important; font-size: 12px !important; }

/* ── ALERTS ── */
div[data-testid="stAlert"] { border-radius: 4px !important; font-size: 14px !important; padding: 10px 14px !important; }
.stSuccess { background: rgba(3,166,109,0.1) !important; border: 1px solid rgba(3,166,109,0.3) !important; color: #03a66d !important; }
.stWarning { background: rgba(240,185,11,0.08) !important; border: 1px solid rgba(240,185,11,0.3) !important; color: #f0b90b !important; }
.stError   { background: rgba(207,48,74,0.08) !important; border: 1px solid rgba(207,48,74,0.3) !important; color: #cf304a !important; }
.stInfo    { background: rgba(24,144,255,0.08) !important; border: 1px solid rgba(24,144,255,0.3) !important; color: #1890ff !important; }

/* ── CHAT MESSAGES ── */
[data-testid="stChatMessage"] { background: #1e2026 !important; border: 1px solid #2b2f36 !important; border-radius: 4px !important; margin-bottom: 6px !important; }
[data-testid="stChatMessage"] p { color: #eaecef !important; }

/* ── CHARTS ── */
[data-testid="stArrowVegaLiteChart"] { background: #1e2026 !important; border-radius: 4px !important; border: 1px solid #2b2f36 !important; padding: 8px !important; }

/* ── MARKDOWN ── */
.stMarkdown p { color: #848e9c !important; }
.stMarkdown strong { color: #eaecef !important; }
.stMarkdown a { color: #f0b90b !important; text-decoration: none !important; }

/* ── CHECKBOX ── */
label[data-testid="stCheckbox"] span { color: #848e9c !important; font-size: 14px !important; }

/* ── LINK BUTTON ── */
a[data-testid="stLinkButton"] {
    background: #2b2f36 !important;
    border: 1px solid #363c45 !important;
    color: #f0b90b !important;
    border-radius: 4px !important;
    font-size: 13px !important;
    font-weight: 500 !important;
}
a[data-testid="stLinkButton"]:hover { background: rgba(240,185,11,0.1) !important; border-color: #f0b90b !important; }

/* ── DIVIDER ── */
hr { border: none !important; border-top: 1px solid #2b2f36 !important; margin: 16px 0 !important; }

/* ── CAPTION ── */
small, .stCaption { color: #474d57 !important; font-size: 12px !important; font-family: 'IBM Plex Mono', monospace !important; }

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: #0b0e11; }
::-webkit-scrollbar-thumb { background: #363c45; border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: #f0b90b; }

/* ── HIDE BRANDING ── */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
</style>
""", unsafe_allow_html=True)'''

with open('app.py', 'r') as f:
    content = f.read()

start = content.find('st.markdown("""')
end   = content.find('""", unsafe_allow_html=True)', start) + len('""", unsafe_allow_html=True)')

if start == -1 or end == -1:
    print("❌ Could not find CSS block")
else:
    new_content = content[:start] + NEW_CSS + content[end:]
    with open('app.py', 'w') as f:
        f.write(new_content)
    print("✅ CSS replaced!")
    print("▶ Run: streamlit run app.py")
