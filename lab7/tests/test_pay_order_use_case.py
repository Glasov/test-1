import pytest
from decimal import Decimal
from domain.order import Order
from domain.money import Money
from application.pay_order_use_case import PayOrderUseCase
from infrastructure.in_memory_order_repository import InMemoryOrderRepository
from infrastructure.fake_payment_gateway import FakePaymentGateway

def create_order_with_items(order_id="order1", customer_id="customer1"):
    order = Order(id=order_id, customer_id=customer_id)
    order.add_line("prod1", "Product 1", 2, Money(Decimal("10.00")))
    order.add_line("prod2", "Product 2", 1, Money(Decimal("5.00")))
    return order

class TestPayOrderUseCase:
    def test_successful_payment(self):
        order = create_order_with_items()
        repo = InMemoryOrderRepository()
        repo.save(order)
        gateway = FakePaymentGateway()
        use_case = PayOrderUseCase(repo, gateway)
        
        result = use_case.execute("order1")
        
        assert result["success"] == True
        assert result["order_id"] == "order1"
        assert repo.get_by_id("order1").is_paid == True
    
    def test_cannot_pay_empty_order(self):
        order = Order(id="order2", customer_id="customer1")
        repo = InMemoryOrderRepository()
        repo.save(order)
        gateway = FakePaymentGateway()
        use_case = PayOrderUseCase(repo, gateway)
        
        result = use_case.execute("order2")
        
        assert result["success"] == False
        assert "empty" in result["error"].lower()
    
    def test_cannot_pay_already_paid_order(self):
        order = create_order_with_items("order3")
        order.pay()  # Сначала оплачиваем
        repo = InMemoryOrderRepository()
        repo.save(order)
        gateway = FakePaymentGateway()
        use_case = PayOrderUseCase(repo, gateway)
        
        result = use_case.execute("order3")
        
        assert result["success"] == False
        assert "already" in result["error"].lower()
    
    def test_correct_total_calculation(self):
        order = create_order_with_items("order4")
        total = order.get_total()
        assert total.amount == Decimal("25.00")  # 2*10 + 1*5 = 25
    
    def test_order_not_found(self):
        repo = InMemoryOrderRepository()
        gateway = FakePaymentGateway()
        use_case = PayOrderUseCase(repo, gateway)
        
        result = use_case.execute("nonexistent")
        
        assert result["success"] == False
        assert "not found" in result["error"].lower()
