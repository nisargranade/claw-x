# utils/llm.py
import requests
from config.settings import OPENROUTER_API_KEY

# Pick your model from openrouter.ai/models
# Free options: "mistralai/mistral-7b-instruct" or "google/gemma-3-27b-it:free"
# Paid (better): "anthropic/claude-3.5-sonnet" or "openai/gpt-4o-mini"
DEFAULT_MODEL = "deepseek/deepseek-chat-v3-0324"

def ask_llm(prompt: str, system: str = "", model: str = DEFAULT_MODEL) -> str:
    """
    Send a message to any LLM via OpenRouter.
    Returns the text response as a plain string.
    """
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:5000",  # Required by OpenRouter
            "X-Title": "OpenClaw AI",                 # Shows up in your dashboard
        },
        json={
            "model": model,
            "messages": messages,
            "temperature": 0.3,
        },
        timeout=30,
    )

    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
