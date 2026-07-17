def validate_order(symbol, side, order_type, quantity, price=None):
    """
    Validate user input before sending it to Binance.
    """

    # Check symbol
    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    # Convert to uppercase
    side = side.upper()
    order_type = order_type.upper()

    # Validate side
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")

    # Validate order type
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")

    # Validate quantity
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    # LIMIT order requires price
    if order_type == "LIMIT":

        if price is None:
            raise ValueError("LIMIT order requires a price.")

        if price <= 0:
            raise ValueError("Price must be greater than zero.")

    return True
