# trading_bot
CLI-based Binance Futures Testnet trading bot with MARKET, LIMIT, and STOP orders.
# Binance Futures Trading Bot (Testnet)

##  Overview

This project is a Python-based CLI trading bot that interacts with Binance Futures Testnet.
It allows users to place MARKET, LIMIT, and STOP (conditional) orders using Binance APIs.

The application is designed with modular structure, input validation, logging, and proper error handling to simulate a real-world backend trading system.

---

##  Features

* Place MARKET orders (instant execution)
* Place LIMIT orders (price-based execution)
* Place STOP orders (conditional trigger)
* CLI-based interaction using arguments
* Input validation for safe execution
* Logging of API requests, responses, and errors
* Structured and reusable code design

---

##  Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance client setup
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── bot.log                # Log file (generated)
├── requirements.txt
├── README.md
```

---

##  Setup Instructions

### 1. Clone the repository

```
git clone <https://github.com/kalyanramagani/Trading_bot/tree/main>
cd trading_bot
```

### 2. Create virtual environment (recommended)

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Get API Keys (Testnet only)

* Go to: https://testnet.binancefuture.com
* Login (GitHub recommended)
* Create API Key and Secret

### 5. Add API Keys

Update your `client.py` or config with:

```
api_key = "YOUR_API_KEY"
api_secret = "YOUR_SECRET_KEY"
```

---

##  Usage

### 🔹 MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### 🔹 LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000
```

### 🔹 STOP Order

```
python cli.py --symbol BTCUSDT --side SELL --type STOP --quantity 0.01 --price 58000 --stop_price 59000
```

---

##  Sample Output

```
ORDER SUCCESS
Order ID: 12345
Status: FILLED
Executed Qty: 0.01
Avg Price: 60200
```

For STOP orders:

```
STOP ORDER PLACED (Waiting for trigger)
Algo ID: 1000000XXXX
Status: NEW
Trigger Price: 59000
```

---

##  Logging

All logs are stored in:

```
bot.log
```

Logs include:

* Order requests
* API responses
* Errors and exceptions

Example:

```
2026-04-16 10:30:01 - INFO - Placing order BTCUSDT BUY MARKET 0.01
2026-04-16 10:30:02 - INFO - Order response: FILLED
```

---

##  Assumptions

* Uses Binance Futures Testnet only (no real money involved)
* API keys are valid and correctly configured
* User provides valid CLI inputs

---

##  Tech Stack

* Python 3.x
* python-binance
* argparse (CLI handling)
* logging module

---

##  Conclusion

This project demonstrates API integration, modular code design, CLI development, and handling of real-world trading workflows using Binance Futures Testnet.

---
