from abc import ABC, abstractmethod

class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None
    def __str__(self):
        return f"{self.dough}, {self.sauce}, {self.topping}"

class PizzaBuilder(ABC):
    @abstractmethod
    def build_dough(self):
        pass
    @abstractmethod
    def build_sauce(self):
        pass
    @abstractmethod
    def build_topping(self):
        pass
    @abstractmethod
    def get_result(self) -> Pizza:
        pass

class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()
    def build_dough(self):
        print("Making dough")
        self.pizza.dough = "Thin"
    def build_sauce(self):
        print("Adding sauce")
        self.pizza.sauce = "Sweet"
    def build_topping(self):
        print("Adding topping")
        self.pizza.topping = "Ham + Pineapple"
    def get_result(self) -> Pizza:
        return self.pizza

class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder
    def construct(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()

if __name__ == '__main__':
    # проверяем, что объект собирается поэтапно
    builder = HawaiianPizzaBuilder()
    director = PizzaDirector(builder)
    director.construct()
    pizza = builder.get_result()
    print(pizza)