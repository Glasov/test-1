cat > strategy.py << 'EOF'
class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплата {amount} руб. кредитной картой"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Оплата {amount} руб. через PayPal"

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.strategy = None
    
    def set_payment_strategy(self, strategy):
        self.strategy = strategy
    
    def add_item(self, item):
        self.items.append(item)
    
    def checkout(self):
        total = sum(self.items)
        return self.strategy.pay(total)

# Пример
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item(100)
    cart.add_item(200)
    
    cart.set_payment_strategy(CreditCardPayment())
    print(cart.checkout())
EOF