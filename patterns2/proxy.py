class Proxy:
    def __init__(self, real):
        self.real = real
    def operation(self):
        if not self.real: self.real = Real()
        return self.real.operation()
