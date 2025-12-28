class Money:
    def __init__(self, amount: float, currency: str = 'USD'):
        if amount < 0:
            raise ValueError('Amount cannot be negative')
        self.amount = amount
        self.currency = currency

    def add(self, other: 'Money') -> 'Money':
        if self.currency != other.currency:
            raise ValueError('Different currencies')
        return Money(self.amount + other.amount, self.currency)