# trade_executor.py
import requests
import json

API_URL = "https://paper-api.alpaca.markets/v2/orders"
API_KEY = "your_alpaca_api_key"
API_SECRET = "your_alpaca_api_secret"
HEADERS = {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": API_SECRET,
    "Content-Type": "application/json"
}

def execute_trade():
    order = {
        "symbol": "AAPL",
        "qty": 1,
        "side": "buy",
        "type": "market",
        "time_in_force": "gtc"
    }
    response = requests.post(API_URL, headers=HEADERS, json=order)
    print("Trade executed:", response.json())

def monitor_trades():
    response = requests.get("https://paper-api.alpaca.markets/v2/positions", headers=HEADERS)
    print("Current positions:", response.json())

def alert_on_trade():
    print("Trade alert: Check your Alpaca dashboard for trade updates.")
