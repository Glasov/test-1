from singleton.logger import Logger
from factory_method.transport_factory import RoadLogistics, SeaLogistics, AirLogistics
from abstract_factory.ui_factory import WindowsFactory, MacFactory, Application
from builder.pizza_builder import Director, MargheritaBuilder, PepperoniBuilder

def test_singleton():
    print("\n" + "="*50)
    print("1. ТЕСТИРОВАНИЕ SINGLETON")
    print("="*50)
    
    logger1 = Logger()
    logger2 = Logger()
    
    logger1.log("Первое сообщение")
    logger2.log("Второе сообщение")
    
    print(f"logger1 is logger2: {logger1 is logger2}")
    print(f"Все сообщения: {logger1.get_logs()}")

def test_factory_method():
    print("\n" + "="*50)
    print("2. ТЕСТИРОВАНИЕ FACTORY METHOD")
    print("="*50)
    
    road_logistics = RoadLogistics()
    print(road_logistics.plan_delivery())
    
    sea_logistics = SeaLogistics()
    print(sea_logistics.plan_delivery())
    
    air_logistics = AirLogistics()
    print(air_logistics.plan_delivery())

def test_abstract_factory():
    print("\n" + "="*50)
    print("3. ТЕСТИРОВАНИЕ ABSTRACT FACTORY")
    print("="*50)
    
    windows_factory = WindowsFactory()
    windows_app = Application(windows_factory)
    print(f"Windows: {windows_app.paint()}")
    
    mac_factory = MacFactory()
    mac_app = Application(mac_factory)
    print(f"MacOS: {mac_app.paint()}")

def test_builder():
    print("\n" + "="*50)
    print("4. ТЕСТИРОВАНИЕ BUILDER")
    print("="*50)
    
    director = Director()
    
    margherita_builder = MargheritaBuilder()
    director.set_builder(margherita_builder)
    margherita = director.make_pizza()
    print(f"Маргарита: {margherita}")
    
    pepperoni_builder = PepperoniBuilder()
    director.set_builder(pepperoni_builder)
    pepperoni = director.make_pizza()
    print(f"Пепперони: {pepperoni}")

def main():
    print("ЛАБОРАТОРНАЯ РАБОТА №3")
    print("ПОРОЖДАЮЩИЕ ПАТТЕРНЫ ПРОЕКТИРОВАНИЯ")
    
    test_singleton()
    test_factory_method()
    test_abstract_factory()
    test_builder()
    
    print("\n" + "="*50)
    print("ВСЕ ПАТТЕРНЫ УСПЕШНО ПРОТЕСТИРОВАНЫ!")
    print("="*50)

if __name__ == "__main__":
    main()
