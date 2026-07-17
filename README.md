# Binance Futures Trading Bot

This is a simple command-line trading bot built in Python using the Binance Futures Testnet API.

The bot allows users to place MARKET and LIMIT orders. It also validates user input, logs API activity, and handles errors.

## Features

- Place MARKET orders
- Place LIMIT orders
- Supports BUY and SELL orders
- Input validation
- Logging
- Exception handling

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
├── main.py
├── README.md
└── requirements.txt
```

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project folder and add your Binance Testnet API credentials.

```
API_KEY=your_api_key
API_SECRET=your_api_secret
```

## Running the Program

Run the following command:

```bash
python main.py
```

The program will ask for:

- Symbol
- Side (BUY/SELL)
- Order Type (MARKET/LIMIT)
- Quantity
- Price (only for LIMIT orders)

## Log File

All order information and errors are saved in:

```
logs/trading_bot.log
```

## Requirements

- Python 3
- Binance Futures Testnet account
- API Key and Secret