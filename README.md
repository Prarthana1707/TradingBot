# Binance Futures Trading Bot

## Overview

This project is a command-line trading bot developed in Python using the Binance Futures Testnet API.

The application allows users to place MARKET and LIMIT orders through a simple menu-driven interface. It validates user inputs, communicates with the Binance Futures Testnet, logs order details, and handles exceptions gracefully.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL orders
- Menu-driven command-line interface
- Input validation
- Logging of orders and errors
- Exception handling

---

## Project Structure

```
TradingBot/
│
├── bot/
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading_bot.log
│
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

## Prerequisites

Before running the project, make sure you have:

- Python 3 installed
- A Binance Futures Testnet account
- Binance Testnet API Key and Secret

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Prarthana1707/TradingBot.git
```

Move to the project directory:

```bash
cd TradingBot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project directory and add your Binance Testnet API credentials:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## Running the Application

Run the following command:

```bash
python main.py
```

After starting the application, a menu will be displayed.

Users can:

- Place a MARKET order
- Place a LIMIT order
- Exit the application

For each order, the program requests:

- Trading Symbol
- Order Side (BUY/SELL)
- Quantity
- Price (for LIMIT orders)

After an order is processed, the user can place another order or exit the application.

---

## Logging

All successful orders and application errors are stored in:

```
logs/trading_bot.log
```

---

## Dependencies

- python-binance
- python-dotenv

(See `requirements.txt` for the complete list.)

---

## Notes

This project uses the Binance Futures **Testnet** for testing purposes. No real trades are executed.