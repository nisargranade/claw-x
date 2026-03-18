with open('app.py', 'r') as f:
    content = f.read()

# Find where sidebar starts
idx = content.find("with st.sidebar:")
if idx == -1:
    print("❌ Could not find 'with st.sidebar:'")
else:
    # Inject style fix right after "with st.sidebar:"
    inject = """with st.sidebar:
    st.markdown(\"\"\"
    <style>
    section[data-testid="stSidebar"] button,
    section[data-testid="stSidebar"] button:focus,
    section[data-testid="stSidebar"] button:active {
        background: transparent !important;
        background-color: transparent !important;
        color: #848e9c !important;
        border: none !important;
        box-shadow: none !important;
        font-size: 14px !important;
        text-align: left !important;
        padding: 8px 12px !important;
        width: 100% !important;
        display: block !important;
        margin-bottom: 2px !important;
        font-weight: 400 !important;
    }
    section[data-testid="stSidebar"] button:hover {
        background: #2b2f36 !important;
        background-color: #2b2f36 !important;
        color: #eaecef !important;
    }
    section[data-testid="stSidebar"] button p {
        color: inherit !important;
        font-size: 14px !important;
    }
    </style>
    \"\"\", unsafe_allow_html=True)"""

    old = "with st.sidebar:"
    content = content.replace(old, inject, 1)

    with open('app.py', 'w') as f:
        f.write(content)
    print("✅ Done! Run: streamlit run app.py")
