class Adaptee:
    def specific_request(self): return "Адаптируемый"
class Adapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee
    def request(self):
        return self.adaptee.specific_request()
