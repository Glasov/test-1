from application.interfaces import OrderRepository

class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self._orders = {}

    def get_by_id(self, order_id: str):
        if order_id not in self._orders:
            raise ValueError('Order not found')
        return self._orders[order_id]

    def save(self, order):
        self._orders[order.order_id] = order
