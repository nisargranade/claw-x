# main.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "🐾 OpenClaw AI is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    # For now, just echo back — we'll add the LLM router next
    return jsonify({"response": f"You said: {message}"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
