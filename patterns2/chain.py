cat > chain_of_responsibility.py << 'EOF'
class Handler:
    def __init__(self):
        self.next = None
    
    def set_next(self, handler):
        self.next = handler
        return handler
    
    def handle(self, request):
        if self.next:
            return self.next.handle(request)
        return None

class TechnicalSupport(Handler):
    def handle(self, request):
        if request == "техническая":
            return "Техподдержка решает проблему"
        return super().handle(request)

class BillingSupport(Handler):
    def handle(self, request):
        if request == "биллинг":
            return "Биллинг решает проблему"
        return super().handle(request)

class GeneralSupport(Handler):
    def handle(self, request):
        return "Общая поддержка решает проблему"

# Пример
if __name__ == "__main__":
    tech = TechnicalSupport()
    billing = BillingSupport()
    general = GeneralSupport()
    
    tech.set_next(billing).set_next(general)
    
    print(tech.handle("техническая"))
    print(tech.handle("биллинг"))
EOF