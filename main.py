from bot.orders import place_order


def display_menu():
    print("\n" + "=" * 45)
    print("      BINANCE FUTURES TRADING BOT")
    print("=" * 45)
    print("1. Place MARKET Order")
    print("2. Place LIMIT Order")
    print("3. Exit")
    print("=" * 45)


def get_order_details(order_type):
    symbol = input("Enter Symbol (e.g. BTCUSDT): ").upper()

    while True:
        side = input("Enter Side (BUY/SELL): ").upper()
        if side in ["BUY", "SELL"]:
            break
        print("Invalid input! Please enter BUY or SELL.")

    while True:
        try:
            quantity = float(input("Enter Quantity: "))
            if quantity > 0:
                break
            print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    price = None

    if order_type == "LIMIT":
        while True:
            try:
                price = float(input("Enter Limit Price: "))
                if price > 0:
                    break
                print("Price must be greater than 0.")
            except ValueError:
                print("Please enter a valid price.")

    return symbol, side, quantity, price


def display_response(order):
    print("\n" + "=" * 45)
    print("ORDER RESPONSE")
    print("=" * 45)
    print(f"Order ID      : {order['orderId']}")
    print(f"Status        : {order['status']}")
    print(f"Symbol        : {order['symbol']}")
    print(f"Side          : {order['side']}")
    print(f"Order Type    : {order['type']}")
    print(f"Quantity      : {order['origQty']}")
    print(f"Executed Qty  : {order['executedQty']}")
    print(f"Price         : {order['price']}")
    print("=" * 45)
    print("Order placed successfully!")
    print("=" * 45)


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            order_type = "MARKET"

        elif choice == "2":
            order_type = "LIMIT"

        elif choice == "3":
            print("\nThank you for using Binance Trading Bot.")
            break

        else:
            print("\nInvalid choice! Please enter 1, 2 or 3.")
            continue

        try:
            symbol, side, quantity, price = get_order_details(order_type)

            print("\n" + "=" * 45)
            print("ORDER REQUEST")
            print("=" * 45)
            print(f"Symbol     : {symbol}")
            print(f"Side       : {side}")
            print(f"Order Type : {order_type}")
            print(f"Quantity   : {quantity}")

            if order_type == "LIMIT":
                print(f"Price      : {price}")

            print("=" * 45)

            order = place_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )

            display_response(order)

        except Exception as e:
            print(f"\nError: {e}")

        again = input("\nDo you want to place another order? (Y/N): ").upper()

        if again != "Y":
            print("\nThank you for using Binance Trading Bot.")
            break


if __name__ == "__main__":
    main()