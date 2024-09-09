from typing import Protocol


class ExecutionException(Exception):
    pass


class ExecutionClient(Protocol):
    def buy(self, product_id: str, amount: int):
        """
        Execute a buy order, throws ExecutionException on failure.
        :param product_id: The product to buy.
        :param amount: The amount to buy.
        :return: None
        """
        raise NotImplementedError

    def sell(self, product_id: str, amount: int):
        """
        Execute a sell order, throws ExecutionException on failure.
        :param product_id: The product to sell.
        :param amount: The amount to sell.
        :return: None
        """
        raise NotImplementedError

