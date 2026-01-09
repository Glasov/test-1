class Strategy:
    def execute(self): pass
class ConcreteStrategy(Strategy):
    def execute(self): return "Стратегия"
