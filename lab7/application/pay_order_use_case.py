from domain.order import Order
from .interfaces import OrderRepository, PaymentGateway

class PayOrderUseCase:
    def __init__(self, order_repo: OrderRepository, payment_gateway: PaymentGateway):
        self.order_repo = order_repo
        self.payment_gateway = payment_gateway
    
    def execute(self, order_id: str) -> dict:
        order = self.order_repo.get_by_id(order_id)
        if not order:
            return {"success": False, "error": "Order not found"}
        
        try:
            order.pay()
        except ValueError as e:
            return {"success": False, "error": str(e)}
        
        total = order.get_total()
        if not self.payment_gateway.charge(order_id, total):
            return {"success": False, "error": "Payment failed"}
        
        self.order_repo.save(order)
        return {"success": True, "order_id": order_id, "amount": str(total)}
