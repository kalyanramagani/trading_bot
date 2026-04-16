import argparse
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logger
import logging

setup_logger()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop_price", type=float)

    args = parser.parse_args()

    validate_input(args.symbol, args.side, args.type, args.quantity, args.price, args.stop_price)

    client = BinanceClient("MtP6HxKegVIFEtL0p94unjkoGtIeTko5v7L6fF3V7q5Gid9QdDcnXP25D0RVMnYy", "jORjyjjwInzFkks9mCKXdpHqSyAzkpgeaG9YJ0P08OC1vdaRgI5mUh31rkutWLUd").client
    # print(client.futures_account_balance())

    logging.info(f"Placing order: {args.symbol} {args.side} {args.type} {args.quantity} {args.price} {args.stop_price}")
    order = place_order(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price,
        args.stop_price)
    
    # print(order)
    if "algoId" in order:
        print("\n STOP ORDER PLACED (Waiting for trigger)")
        print(f"Algo ID: {order.get('algoId')}")
        print(f"Status: {order.get('algoStatus')}")
        print(f"Trigger Price: {order.get('triggerPrice')}")
        print(f"Order Price: {order.get('price')}")

    elif "orderId" in order:
        print("\n ORDER EXECUTED")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")

    logging.info(f"Order response: {order}")
    print(logging.basicConfig())

if __name__ == "__main__":
    main()