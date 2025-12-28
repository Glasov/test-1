import pytest
from domain import Order, OrderLine, Money
from application.pay_order_use_case import PayOrderUseCase
from infrastructure.in_memory_order_repository import InMemoryOrderRepository
from infrastructure.fake_payment_gateway import FakePaymentGateway


def create_order():
    lines = [
        OrderLine('product-1', Money(50), 2),
        OrderLine('product-2', Money(30), 1),
    ]
    return Order('order-1', lines)


def test_successful_payment():
    repo = InMemoryOrderRepository()
    gateway = FakePaymentGateway()
    order = create_order()
    repo.save(order)

    use_case = PayOrderUseCase(repo, gateway)
    result = use_case.execute(order.order_id)

    assert result['status'] == 'paid'
    assert result['total'] == 130


def test_empty_order_payment_error():
    repo = InMemoryOrderRepository()
    gateway = FakePaymentGateway()
    order = Order('order-2', [])
    repo.save(order)

    use_case = PayOrderUseCase(repo, gateway)
    with pytest.raises(ValueError):
        use_case.execute(order.order_id)


def test_double_payment_error():
    repo = InMemoryOrderRepository()
    gateway = FakePaymentGateway()
    order = create_order()
    repo.save(order)

    use_case = PayOrderUseCase(repo, gateway)
    use_case.execute(order.order_id)

    with pytest.raises(ValueError):
        use_case.execute(order.order_id)


def test_cannot_modify_paid_order():
    order = create_order()
    order.pay()

    with pytest.raises(ValueError):
        order.add_line(OrderLine('new', Money(10), 1))


def test_total_calculation():
    order = create_order()
    assert order.total().amount == 130
