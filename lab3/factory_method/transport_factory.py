from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        return "Доставка груза по дороге на грузовике"

class Ship(Transport):
    def deliver(self):
        return "Доставка груза по морю на корабле"

class Plane(Transport):
    def deliver(self):
        return "Доставка груза по воздуху на самолете"

class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass
    
    def plan_delivery(self):
        transport = self.create_transport()
        return f"Планирование доставки: {transport.deliver()}"

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

class AirLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Plane()
