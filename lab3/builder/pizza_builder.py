class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.toppings = []
        self.cheese = ""
    
    def __str__(self):
        return f"Пицца: тесто={self.dough}, соус={self.sauce}, " \
               f"начинка={', '.join(self.toppings) if self.toppings else 'нет'}, " \
               f"сыр={self.cheese}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def build_dough(self):
        pass
    
    def build_sauce(self):
        pass
    
    def build_toppings(self):
        pass
    
    def build_cheese(self):
        pass
    
    def get_pizza(self):
        return self.pizza

class MargheritaBuilder(PizzaBuilder):
    def build_dough(self):
        self.pizza.dough = "тонкое"
    
    def build_sauce(self):
        self.pizza.sauce = "томатный"
    
    def build_toppings(self):
        self.pizza.toppings = ["помидоры", "базилик"]
    
    def build_cheese(self):
        self.pizza.cheese = "моцарелла"

class PepperoniBuilder(PizzaBuilder):
    def build_dough(self):
        self.pizza.dough = "толстое"
    
    def build_sauce(self):
        self.pizza.sauce = "острый томатный"
    
    def build_toppings(self):
        self.pizza.toppings = ["пепперони", "перец", "лук"]
    
    def build_cheese(self):
        self.pizza.cheese = "чеддер и моцарелла"

class Director:
    def __init__(self):
        self.builder = None
    
    def set_builder(self, builder: PizzaBuilder):
        self.builder = builder
    
    def make_pizza(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_toppings()
        self.builder.build_cheese()
        return self.builder.get_pizza()
