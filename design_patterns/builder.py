class Car:
    def __init__(self):
        self.engine = None
        self.seats = None

class CarBuilder:
    def __init__(self):
        self.car = Car()
    
    def set_engine(self, engine):
        self.car.engine = engine
        return self
    
    def set_seats(self, seats):
        self.car.seats = seats
        return self
    
    def build(self):
        return self.car
