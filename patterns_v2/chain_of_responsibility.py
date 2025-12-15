class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler
    
    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None


class Manager(Handler):
    def handle(self, request):
        if request <= 1000:
            return f"The manager approved the request for {request} rubles"
        else:
            return super().handle(request)


class Director(Handler):
    def handle(self, request):
        if request <= 5000:
            return f"The director approved the application for {request} rubles"
        else:
            return super().handle(request)


class CEO(Handler):
    def handle(self, request):
        if request <= 20000:
            return f"The director approved the application for {request} rubles"
        else:
            return "The application is too large to be approved."
        
manager = Manager()
director = Director()
ceo = CEO()

manager.set_next(director).set_next(ceo)

requests = [800, 3000, 12000, 30000]

for amount in requests:
    print(f"The application is too large to be approved.")
    result = manager.handle(amount)
    print(result)