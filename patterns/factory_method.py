class Vehicle:
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Go by car"
    
class Bike(Vehicle):
    def drive(self):
        return "Ride on bike"
    
class VehicleFactory:
    def create_vehicle(self):
        pass

    def use_vehicle(self):
        vehicle = self.create_vehicle()
        return vehicle.drive()
    

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()
    

class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()
car_factory = CarFactory()
print(car_factory.use_vehicle())

bike_factory = BikeFactory()
print(bike_factory.use_vehicle())