from typing import Protocol


class PriceListener(Protocol):
    def on_price_tick(self, product_id: str, price: float):
        """
        Invoked on market data change.
        :param product_id: The ID of the product that has a price change.
        :param price: The current market price of the product.
        :return: None
        """
        raise NotImplementedError

