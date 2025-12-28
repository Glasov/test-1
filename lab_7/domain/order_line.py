from domain.money import Money

class OrderLine:
    def __init__(self, product: str, price: Money, quantity: int):
        if quantity <= 0:
            raise ValueError('Quantity must be positive')
        if price.amount <= 0:
            raise ValueError('Price must be positive')
        self.product = product
        self.price = price
        self.quantity = quantity

    def total(self) -> Money:
        return Money(self.price.amount * self.quantity, self.price.currency)
