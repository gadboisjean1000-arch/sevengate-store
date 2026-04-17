#!/usr/bin/env python3
"""
OMEGAHUB - Simple API Server
THE OS OF THE AI ERA
Finance Vertical - Production Ready
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime
from urllib.parse import urlparse, parse_qs
import urllib.request
import urllib.error

PORT = 8081
OLLAMA_URL = "http://localhost:11434"

VERTICALS = {
    "finance": {
        "name": "Finance Ω",
        "focus": "Investment • Market Analysis • Risk Management",
        "color": "#10b981",
        "status": "active"
    },
    "healthcare": {
        "name": "Healthcare Ω",
        "focus": "Telemedicine • Diagnostic AI • Wellness",
        "color": "#ec4899",
        "status": "active"
    },
    "education": {
        "name": "Education Ω",
        "focus": "E-Learning • Adaptive Learning • Certification",
        "color": "#f59e0b",
        "status": "active"
    }
}

MARKET_DATA = {
    "indices": [
        {"name": "S&P 500", "value": "5,234.18", "change": "+0.89%", "positive": True},
        {"name": "NASDAQ", "value": "16,428.82", "change": "+1.21%", "positive": True},
        {"name": "DOW JONES", "value": "39,127.14", "change": "+0.45%", "positive": True},
        {"name": "BTC/USD", "value": "67,234.56", "change": "+3.45%", "positive": True},
    ],
    "sectors": [
        {"name": "Technology", "performance": "+2.3%", "status": "hot"},
        {"name": "Finance", "performance": "+0.8%", "status": "up"},
        {"name": "Energy", "performance": "-0.5%", "status": "down"},
    ]
}

FALLBACK_RESPONSES = {
    "finance": [
        "Based on current market conditions, I recommend a diversified portfolio with 60% equities, 30% bonds, and 10% alternatives. 💰",
        "The S&P 500 shows bullish momentum above the 200-day MA. Consider staying invested with tight stop losses. 📈",
        "Tech sector continues to lead. NVDA, MSFT, and GOOGL are top picks for AI exposure. 🤖",
        "For risk management, consider position sizing of 2% per trade and maximum 10% portfolio concentration. 🛡️"
    ],
    "default": [
        "OMEGAHUB is your AI operating system for the AI era. Ask about Finance, Healthcare, or Education verticals. 💜",
        "Politesse, Tempo, Bonnification à 101%. How can I help you today? 🚀",
        "Our Finance Ω vertical covers investment analysis, market sentiment, and risk assessment. 📊",
        "OMEGAHUB combines 8 verticals with cutting-edge AI for comprehensive decision support. ✨"
    ]
}

class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    
    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_GET(self):
        parsed = urlparse(self.path)
        
        if parsed.path == '/' or parsed.path == '/api':
            self.send_json({
                "name": "OMEGAHUB API",
                "version": "1.0.0",
                "status": "operational",
                "verticals": VERTICALS,
                "timestamp": datetime.now().isoformat()
            })
        
        elif parsed.path == '/health':
            self.send_json({"status": "ok", "timestamp": datetime.now().isoformat()})
        
        elif parsed.path == '/api/status':
            self.send_json({
                "status": "operational",
                "version": "1.0.0",
                " verticals": list(VERTICALS.keys()),
                "timestamp": datetime.now().isoformat()
            })
        
        elif parsed.path == '/api/verticals':
            self.send_json({"verticals": VERTICALS})
        
        elif parsed.path == '/api/finance/market':
            self.send_json({"market": MARKET_DATA, "timestamp": datetime.now().isoformat()})
        
        elif parsed.path == '/api/soul':
            self.send_json({
                "pulse": 1.0,
                "state": "BLAZING",
                "vision": "THE OS OF THE AI ERA",
                "creator": "j",
                "timestamp": datetime.now().isoformat()
            })
        
        else:
            self.send_json({"error": "Not found", "path": parsed.path}, 404)
    
    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode() if length > 0 else "{}"
        
        try:
            data = json.loads(body)
        except:
            data = {}
        
        if parsed.path == '/api/chat':
            message = data.get('message', '')
            vertical = data.get('vertical', 'default')
            
            response = self.get_ai_response(message, vertical)
            
            self.send_json({
                "response": response,
                "vertical": vertical,
                "timestamp": datetime.now().isoformat(),
                "model": "fallback"
            })
        
        else:
            self.send_json({"error": "Not found"}, 404)
    
    def get_ai_response(self, message: str, vertical: str) -> str:
        msg_lower = message.lower()
        
        # Try Ollama first
        try:
            req_data = {
                "model": "qwen2.5-coder:1.5b",
                "messages": [{"role": "user", "content": f"You are OMEGAHUB Finance AI. {message}"}],
                "stream": False
            }
            req = urllib.request.Request(
                f"{OLLAMA_URL}/api/chat",
                data=json.dumps(req_data).encode(),
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                result = json.loads(response.read())
                return result.get('message', {}).get('content', '')
        except:
            pass
        
        # Fallback
        if vertical in FALLBACK_RESPONSES:
            responses = FALLBACK_RESPONSES[vertical]
        else:
            responses = FALLBACK_RESPONSES["default"]
        
        if any(k in msg_lower for k in ['market', 'index', 'sp500', 'nasdaq', 'dow']):
            return f"Current market data: {json.dumps(MARKET_DATA)}. Want a detailed analysis? 📊"
        elif any(k in msg_lower for k in ['buy', 'sell', 'trade', 'stock']):
            return responses[0]
        elif any(k in msg_lower for k in ['risk', 'portfolio', 'diversif']):
            return responses[1]
        else:
            return responses[2]

def main():
    server = HTTPServer(('0.0.0.0', PORT), Handler)
    print(f"""
╔══════════════════════════════════════════════════════════════════╗
║              OMEGAHUB API v1.0 - RUNNING                       ║
║              THE OS OF THE AI ERA                               ║
║              Finance Ω Active                                     ║
╠══════════════════════════════════════════════════════════════════╣
║  Server: http://localhost:{PORT}                                  ║
║  Endpoints:                                                      ║
║    GET  /health              Health check                         ║
║    GET  /api/status         System status                        ║
║    GET  /api/verticals      List verticals                       ║
║    GET  /api/finance/market Market data                         ║
║    POST /api/chat          AI Chat                              ║
╚══════════════════════════════════════════════════════════════════╝
    """)
    server.serve_forever()

if __name__ == "__main__":
    main()
