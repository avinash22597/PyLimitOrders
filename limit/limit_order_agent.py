from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener


class LimitOrderAgent(PriceListener):
    def __init__(self, execution_client: ExecutionClient) -> None:
        """
        :param execution_client: Can be used to buy or sell - see ExecutionClient protocol definition.
        """
        super().__init__()
        self.execution_client = execution_client
        self.orders = [] 

    def add_order(self, side: str, product_id: str, amount: int, limit: float):
        """
        Add an order to the agent.
        :param side: "buy" or "sell"
        :param product_id: The product id
        :param amount: The number of shares to buy or sell
        :param limit: The price limit to buy/sell
        """
        order = {
            'side': side,
            'product_id': product_id,
            'amount': amount,
            'limit': limit
        }
        self.orders.append(order)

    def on_price_tick(self, product_id: str, price: float):
        """
        Called when there's a price update. If the price is better or equal to the limit of any order, execute it.
        :param product_id: The product for which the price has changed
        :param price: The new market price of the product
        """
        for order in self.orders:
            if order['product_id'] == product_id:
                if order['side'] == 'buy' and price <= order['limit']:
                    try:
                        self.execution_client.buy(product_id, order['amount'])
                        print(f"Executed buy order for {order['amount']} shares of {product_id} at {price}")
                    except Exception as e:
                        print(f"Error executing buy order: {e}")
                    self.orders.remove(order)
                elif order['side'] == 'sell' and price >= order['limit']:
                    try:
                        self.execution_client.sell(product_id, order['amount'])
                        print(f"Executed sell order for {order['amount']} shares of {product_id} at {price}")
                    except Exception as e:
                        print(f"Error executing sell order: {e}")
                    self.orders.remove(order)
