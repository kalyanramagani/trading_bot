def validate_input(symbol, side, order_type, quantity, price, stop_price=None):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side")
        logging.error(f"Error occurred: {str(e)}")

    if order_type not in ["MARKET", "LIMIT", "STOP"]:
        raise ValueError("Invalid order type")
        logging.error(f"Error occurred: {str(e)}")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT")
        logging.error(f"Error occurred: {str(e)}")

    if order_type == "STOP":
        if price is None or stop_price is None:
            raise ValueError("STOP requires price and stop_price")
            logging.error(f"Error occurred: {str(e)}")