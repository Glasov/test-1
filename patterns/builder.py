class Pizza:
    def __init__(self):
        self.dough = ""
        self.sauce = ""
        self.topping = ""
        self.cheese = ""

    def __str__(self):
        return f"Pizza: dough={self.dough}, sauce={self.sauce}, topping={self.topping}, cheese={self.cheese}"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_dough(self, dough_type):
        self.pizza.dough = dough_type
        return self
    
    def add_sauce(self, sauce_type):
        self.pizza.sauce = sauce_type
        return self
    
    def add_topping(self, topping_type):
        self.pizza.topping = topping_type
        return self
    
    def add_cheese(self, cheese_type):
        self.pizza.cheese = cheese_type
        return self
    
    def get_pizza(self):
        return self.pizza
    

class PizzaCook:
    def make_margherita(self):
        return (PizzaBuilder()
                .add_dough("thin")
                .add_sauce("ketchup")
                .add_topping("tomatoes")
                .add_cheese("mozzarella")
                .get_pizza())
    
    def make_pepperoni(self):
        return (PizzaBuilder()
                .add_dough("thick")
                .add_sauce("ketchup")
                .add_topping("pepperoni")
                .add_cheese("cheddar")
                .get_pizza())
builder = PizzaBuilder()
custom_pizza = (builder
                .add_dough("average")
                .add_sauce("creamy")
                .add_topping("mushrooms")
                .add_cheese("parmesan")
                .get_pizza())

cook = PizzaCook()
margherita = cook.make_margherita()
pepperoni = cook.make_pepperoni()
print(f"Margherita:{margherita}")
print(f"Pepperoni: {pepperoni}")