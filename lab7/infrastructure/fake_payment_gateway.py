from application.interfaces import PaymentGateway
from domain.money import Money

class FakePaymentGateway(PaymentGateway):
    def charge(self, order_id: str, amount: Money) -> bool:
        # Всегда возвращаем успех для тестов
        print(f"Charged {amount} for order {order_id}")
        return True
