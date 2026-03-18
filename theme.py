# theme.py — OpenClaw AI Light Theme
# Usage: add these 2 lines in app.py after st.set_page_config():
#   from theme import apply_theme
#   apply_theme()

import streamlit as st

def apply_theme():
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

    <style>

    /* ── BASE ── */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        background: #f5f7fa !important;
        color: #1a2035 !important;
        font-size: 14px !important;
    }
    .stApp { background: #f5f7fa !important; }

    /* ── SIDEBAR ── */
    [data-testid="stSidebar"] {
        background: #ffffff !important;
        border-right: 1px solid #e2e8f0 !important;
        box-shadow: 2px 0 8px rgba(0,0,0,0.04) !important;
    }
    [data-testid="stSidebar"] * {
        color: #4a5568 !important;
        font-family: 'Inter', sans-serif !important;
    }
    [data-testid="stSidebar"] h2 {
        color: #1a2035 !important;
        font-size: 18px !important;
        font-weight: 700 !important;
    }

    /* ── SIDEBAR BUTTONS ── */
    [data-testid="stSidebar"] button {
        background: transparent !important;
        border: none !important;
        color: #4a5568 !important;
        font-size: 14px !important;
        font-weight: 400 !important;
        text-align: left !important;
        padding: 9px 16px !important;
        margin-bottom: 2px !important;
        border-radius: 8px !important;
        width: 100% !important;
        transition: all 0.15s !important;
        cursor: pointer !important;
    }
    [data-testid="stSidebar"] button:hover {
        background: #f0f4ff !important;
        color: #2563eb !important;
    }
    [data-testid="stSidebar"] button p {
        color: inherit !important;
        font-size: 14px !important;
        margin: 0 !important;
    }

    /* ── HEADINGS ── */
    h1 {
        font-weight: 700 !important;
        font-size: 26px !important;
        color: #1a2035 !important;
        border-bottom: 2px solid #e2e8f0 !important;
        padding-bottom: 12px !important;
        margin-bottom: 8px !important;
    }
    h2 { font-weight: 600 !important; font-size: 20px !important; color: #1a2035 !important; }
    h3 { font-weight: 600 !important; font-size: 15px !important; color: #4a5568 !important; }

    /* ── TEXT ── */
    p { color: #4a5568 !important; font-size: 14px !important; line-height: 1.65 !important; }
    strong { color: #1a2035 !important; font-weight: 600 !important; }
    code {
        font-family: 'JetBrains Mono', monospace !important;
        background: #f0f4ff !important;
        color: #2563eb !important;
        padding: 2px 6px !important;
        border-radius: 4px !important;
        font-size: 12px !important;
        border: 1px solid #dbeafe !important;
    }

    /* ── MAIN BUTTONS ── */
    .stButton > button {
        background: #2563eb !important;
        border: none !important;
        color: #ffffff !important;
        border-radius: 8px !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        padding: 9px 20px !important;
        transition: all 0.15s !important;
        cursor: pointer !important;
        box-shadow: 0 1px 3px rgba(37,99,235,0.3) !important;
    }
    .stButton > button:hover {
        background: #1d4ed8 !important;
        box-shadow: 0 4px 12px rgba(37,99,235,0.35) !important;
        transform: translateY(-1px) !important;
    }

    /* ── INPUTS ── */
    input, textarea,
    div[data-baseweb="input"] input,
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        background: #ffffff !important;
        color: #1a2035 !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 14px !important;
        caret-color: #2563eb !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
    }
    input::placeholder, textarea::placeholder { color: #a0aec0 !important; }
    input:focus, textarea:focus {
        border-color: #2563eb !important;
        box-shadow: 0 0 0 3px rgba(37,99,235,0.1) !important;
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
        background: #ffffff !important;
        background-color: #ffffff !important;
        color: #1a2035 !important;
        caret-color: #2563eb !important;
        border-color: #e2e8f0 !important;
    }
    [data-testid="stChatInput"] textarea::placeholder { color: #a0aec0 !important; }

    /* ── SELECTBOX ── */
    div[data-baseweb="select"] > div {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04) !important;
    }
    div[data-baseweb="select"] span,
    div[data-baseweb="select"] div {
        background: #ffffff !important;
        color: #1a2035 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 14px !important;
    }
    li[role="option"] {
        background: #ffffff !important;
        color: #4a5568 !important;
        font-size: 14px !important;
        padding: 8px 14px !important;
    }
    li[role="option"]:hover, li[aria-selected="true"] {
        background: #f0f4ff !important;
        color: #2563eb !important;
    }

    /* ── NUMBER INPUT ── */
    div[data-testid="stNumberInput"] > div {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
    }
    div[data-testid="stNumberInput"] button {
        background: #f8fafc !important;
        color: #4a5568 !important;
        border: none !important;
    }
    div[data-testid="stNumberInput"] button:hover {
        background: #f0f4ff !important;
        color: #2563eb !important;
    }

    /* ── SLIDER ── */
    div[data-testid="stSlider"] div[role="slider"] {
        background: #2563eb !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 0 6px rgba(37,99,235,0.4) !important;
    }
    div[data-testid="stSlider"] > div > div > div > div {
        background: #2563eb !important;
    }
    div[data-testid="stSlider"] p {
        color: #4a5568 !important;
        font-size: 12px !important;
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* ── METRICS ── */
    div[data-testid="stMetric"] {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 10px !important;
        padding: 18px 20px !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05) !important;
        transition: box-shadow 0.2s !important;
    }
    div[data-testid="stMetric"]:hover {
        box-shadow: 0 4px 16px rgba(37,99,235,0.08) !important;
    }
    div[data-testid="stMetricLabel"] > div {
        color: #718096 !important;
        font-size: 11px !important;
        font-family: 'JetBrains Mono', monospace !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    div[data-testid="stMetricValue"] > div {
        color: #1a2035 !important;
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 24px !important;
        font-weight: 600 !important;
    }
    div[data-testid="stMetricDelta"] > div {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 12px !important;
    }

    /* ── ALERTS ── */
    div[data-testid="stAlert"] {
        border-radius: 8px !important;
        font-size: 14px !important;
        padding: 12px 16px !important;
        font-family: 'Inter', sans-serif !important;
    }
    .stSuccess { background: #f0fdf4 !important; border: 1px solid #bbf7d0 !important; color: #166534 !important; }
    .stInfo    { background: #eff6ff !important; border: 1px solid #bfdbfe !important; color: #1e40af !important; }
    .stWarning { background: #fffbeb !important; border: 1px solid #fde68a !important; color: #92400e !important; }
    .stError   { background: #fef2f2 !important; border: 1px solid #fecaca !important; color: #991b1b !important; }

    /* ── CHAT MESSAGES ── */
    [data-testid="stChatMessage"] {
        background: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 10px !important;
        margin-bottom: 8px !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04) !important;
    }
    [data-testid="stChatMessage"] p { color: #1a2035 !important; font-size: 14px !important; }

    /* ── CHARTS ── */
    [data-testid="stArrowVegaLiteChart"] {
        background: #ffffff !important;
        border-radius: 10px !important;
        border: 1px solid #e2e8f0 !important;
        padding: 8px !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04) !important;
    }

    /* ── MARKDOWN ── */
    .stMarkdown p { color: #4a5568 !important; font-size: 14px !important; }
    .stMarkdown strong { color: #1a2035 !important; }
    .stMarkdown a { color: #2563eb !important; text-decoration: none !important; }
    .stMarkdown a:hover { text-decoration: underline !important; }

    /* ── CHECKBOX ── */
    label[data-testid="stCheckbox"] span { color: #4a5568 !important; font-size: 14px !important; }

    /* ── LINK BUTTON ── */
    a[data-testid="stLinkButton"] {
        background: #f0f4ff !important;
        border: 1px solid #bfdbfe !important;
        color: #2563eb !important;
        border-radius: 6px !important;
        font-size: 13px !important;
        font-weight: 600 !important;
        transition: all 0.15s !important;
    }
    a[data-testid="stLinkButton"]:hover {
        background: #dbeafe !important;
        border-color: #2563eb !important;
    }

    /* ── DIVIDER ── */
    hr { border: none !important; border-top: 1px solid #e2e8f0 !important; margin: 18px 0 !important; }

    /* ── CAPTION ── */
    small, .stCaption {
        color: #a0aec0 !important;
        font-size: 12px !important;
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* ── SCROLLBAR ── */
    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-track { background: #f5f7fa; }
    ::-webkit-scrollbar-thumb { background: #cbd5e0; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #2563eb; }

    /* ── SELECTION ── */
    ::selection { background: #bfdbfe; color: #1e40af; }

    /* ── HIDE BRANDING ── */
    #MainMenu, footer, header { visibility: hidden; }
    .stDeployButton { display: none; }

    </style>
    """, unsafe_allow_html=True)
