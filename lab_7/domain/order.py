from domain.order_status import OrderStatus
from domain.money import Money
from domain.order_line import OrderLine

class Order:
    def __init__(self, order_id: str, lines: list[OrderLine]):
        self.order_id = order_id
        self.lines = lines
        self.status = OrderStatus.PENDING

    def total(self) -> Money:
        if not self.lines:
            return Money(0)
        total = Money(0, self.lines[0].price.currency)
        for line in self.lines:
            total = total.add(line.total())
        return total

    def pay(self):
        if self.status == OrderStatus.PAID:
            raise ValueError('Order already paid')
        if not self.lines:
            raise ValueError('Cannot pay empty order')
        self.status = OrderStatus.PAID

    def add_line(self, line: OrderLine):
        if self.status == OrderStatus.PAID:
            raise ValueError('Cannot modify paid order')
        self.lines.append(line)
