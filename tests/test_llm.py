# tests/test_llm.py
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.llm import ask_llm

response = ask_llm("Say hello and confirm you are working.")
print("LLM Response:", response)
