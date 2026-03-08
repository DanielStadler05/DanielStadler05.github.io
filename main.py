import yfinance as yf
import requests
import json
import time

purchases = [
    {"amount": 10.51, "investedSEK": 3191.18},
    {"amount": 68.54, "investedSEK": 38974.22},
    {"amount": 83.69, "investedSEK": 40003.75}
]

ticker = yf.Ticker("0P00017J97")
price_usd = ticker.history(period="1d")["Close"].iloc[-1]

fx = requests.get(
    "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json"
).json()
usd_sek = fx["usd"]["sek"]

total_shares = sum(p["amount"] for p in purchases)
invested = sum(p["investedSEK"] for p in purchases)

value = total_shares * price_usd * usd_sek
profit = value - invested
return_percent = (profit / invested) * 100

data = {
    "price_usd": price_usd,
    "usd_sek": usd_sek,
    "total_shares": total_shares,
    "invested": invested,
    "value": value,
    "profit": profit,
    "return_percent": return_percent,
    "timestamp": int(time.time())
}

with open("portfolio.json", "w") as f:
    json.dump(data, f, indent=2)

print("portfolio.json updated:", data)