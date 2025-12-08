from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self, destination):
        pass

class Truck(Transport):
    def deliver(self, destination):
        return f"Доставка грузовиком в {destination}"

class Ship(Transport):
    def deliver(self, destination):
        return f"Доставка кораблём в {destination}"

class Plane(Transport):
    def deliver(self, destination):
        return f"Доставка самолётом в {destination}"

# Абстрактная фабрика
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self, destination):
        transport = self.create_transport()
        return transport.deliver(destination)

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

class AirLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Plane()

if __name__ == "__main__":
    print("Планирование доставок:")

    # Наземная логистика
    road = RoadLogistics()
    print(road.plan_delivery("Санкт-Петербург"))

    # Морская логистика
    sea = SeaLogistics()
    print(sea.plan_delivery("Новороссийск"))

    # Воздушная логистика
    air = AirLogistics()
    print(air.plan_delivery("Пекин"))