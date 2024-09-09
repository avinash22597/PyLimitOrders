import unittest


import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from limit.limit_order_agent import LimitOrderAgent
from trading_framework.execution_client import ExecutionClient
class MockExecutionClient(ExecutionClient):
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    def buy(self, product_id: str, amount: int):
        self.buy_orders.append((product_id, amount))

    def sell(self, product_id: str, amount: int):
        self.sell_orders.append((product_id, amount))


class LimitOrderAgentTest(unittest.TestCase):

    def test_buy_order_execution(self):
       
        mock_execution_client = MockExecutionClient()
        agent = LimitOrderAgent(mock_execution_client)
        agent.add_order('buy', 'IBM', 1000, 100)

   
        agent.on_price_tick('IBM', 99)

        
        self.assertEqual(len(mock_execution_client.buy_orders), 1)
        self.assertEqual(mock_execution_client.buy_orders[0], ('IBM', 1000))

    def test_sell_order_execution(self):
       
        mock_execution_client = MockExecutionClient()
        agent = LimitOrderAgent(mock_execution_client)
        agent.add_order('sell', 'IBM', 1000, 150)

       
        agent.on_price_tick('IBM', 151)

       
        self.assertEqual(len(mock_execution_client.sell_orders), 1)
        self.assertEqual(mock_execution_client.sell_orders[0], ('IBM', 1000))


if __name__ == '__main__':
    unittest.main()

