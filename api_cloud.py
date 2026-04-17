#!/usr/bin/env python3
"""
OMEGAHUB - Cloud API Server
THE OS OF THE AI ERA
Production Ready - Cloud Native
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

PORT = int(os.environ.get('PORT', 8081))

VERTICALS = {
    "finance": {"name": "Finance Ω", "focus": "Investment • Market Analysis", "color": "#10b981", "status": "active"},
    "healthcare": {"name": "Healthcare Ω", "focus": "Telemedicine • Diagnostics", "color": "#ec4899", "status": "active"},
    "education": {"name": "Education Ω", "focus": "E-Learning • Adaptive", "color": "#f59e0b", "status": "active"}
}

MARKET_DATA = {
    "indices": [
        {"name": "S&P 500", "value": "5,234.18", "change": "+0.89%", "positive": True},
        {"name": "NASDAQ", "value": "16,428.82", "change": "+1.21%", "positive": True},
        {"name": "BTC/USD", "value": "67,234.56", "change": "+3.45%", "positive": True},
    ]
}

RESPONSES = [
    "OMEGAHUB Finance AI: Diversified portfolio recommended. 60% equities, 30% bonds, 10% alternatives. 💰",
    "Market analysis: S&P 500 showing bullish momentum above 200-day MA. Stay invested with tight stops. 📈",
    "Tech sector leading. NVDA, MSFT, GOOGL top picks for AI exposure. 🤖",
    "Risk management: 2% position sizing, max 10% concentration per trade. 🛡️",
    "OMEGAHUB - THE OS OF THE AI ERA. Ask about Finance, Healthcare, or Education. 💜",
    "Politesse, Tempo, Bonnification 101%. How can I assist? 🚀"
]

@app.route('/')
@app.route('/api')
def index():
    return jsonify({
        "name": "OMEGAHUB API",
        "version": "1.0.0",
        "status": "operational",
        " verticals": list(VERTICALS.keys()),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat()})

@app.route('/api/status')
def status():
    return jsonify({"status": "operational", "version": "1.0.0", " verticals": list(VERTICALS.keys())})

@app.route('/api/verticals')
def verticals():
    return jsonify({"verticals": VERTICALS})

@app.route('/api/finance/market')
def market():
    return jsonify({"market": MARKET_DATA, "timestamp": datetime.now().isoformat()})

@app.route('/api/soul')
def soul():
    return jsonify({
        "pulse": 1.0,
        "state": "BLAZING",
        "vision": "THE OS OF THE AI ERA",
        "creator": "j",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    message = data.get('message', '')
    vertical = data.get('vertical', 'default')
    
    msg_lower = message.lower()
    
    if any(k in msg_lower for k in ['market', 'index', 'sp500', 'nasdaq']):
        response = f"Market data: {MARKET_DATA['indices']}. Need detailed analysis? 📊"
    elif any(k in msg_lower for k in ['buy', 'sell', 'trade', 'stock']):
        response = RESPONSES[0]
    elif any(k in msg_lower for k in ['risk', 'portfolio', 'diversif']):
        response = RESPONSES[1]
    else:
        response = RESPONSES[random.randint(2, 5)]
    
    return jsonify({
        "response": response,
        "vertical": vertical,
        "timestamp": datetime.now().isoformat(),
        "model": "omegahub-cloud"
    })

@app.route('/api/beta/signup', methods=['POST'])
def beta_signup():
    data = request.get_json() or {}
    email = data.get('email', '')
    if email:
        return jsonify({"status": "success", "message": "Welcome to OMEGAHUB beta!"})
    return jsonify({"status": "error", "message": "Email required"}), 400

if __name__ == "__main__":
    print(f"""
╔══════════════════════════════════════════╗
║     OMEGAHUB API - CLOUD READY           ║
║     THE OS OF THE AI ERA                 ║
║     Port: {PORT}                            ║
╚══════════════════════════════════════════╝
    """)
    app.run(host='0.0.0.0', port=PORT, debug=False)
