from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self): pass

class Truck(Transport):
    def deliver(self): return "Доставка грузовиком"

class Logistics(ABC):
    @abstractmethod
    def create_transport(self): pass
    
    def plan(self): 
        return self.create_transport().deliver()

class RoadLogistics(Logistics):
    def create_transport(self): return Truck()
