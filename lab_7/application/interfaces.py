class OrderRepository:
    def get_by_id(self, order_id: str):
        raise NotImplementedError

    def save(self, order):
        raise NotImplementedError


class PaymentGateway:
    def charge(self, order_id: str, money):
        raise NotImplementedError
