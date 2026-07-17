from binance.enums import *
from bot.client import client
from bot.validators import validate_order
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):
    """
    Place a Futures order on Binance Testnet.
    """

    try:
        # Validate user input
        validate_order(symbol, side, order_type, quantity, price)

        if order_type.upper() == "MARKET":

            order = client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )

            # Log MARKET order
            logger.info(
                f"MARKET {side.upper()} | "
                f"Symbol={symbol.upper()} | "
                f"Qty={quantity} | "
                f"OrderID={order['orderId']} | "
                f"Status={order['status']}"
            )

        else:

            order = client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type=FUTURE_ORDER_TYPE_LIMIT,
                quantity=quantity,
                price=price,
                timeInForce=TIME_IN_FORCE_GTC
            )

            # Log LIMIT order
            logger.info(
                f"LIMIT {side.upper()} | "
                f"Symbol={symbol.upper()} | "
                f"Qty={quantity} | "
                f"Price={price} | "
                f"OrderID={order['orderId']} | "
                f"Status={order['status']}"
            )

        return order

    except Exception as e:
        logger.error(str(e))
        raise