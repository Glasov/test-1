"""
Паттерн Мост (Bridge)
Разделяет абстракцию и реализацию, чтобы они могли изменяться независимо.
"""

from abc import ABC, abstractmethod

# Реализация (имплементация)
class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool:
        pass
    
    @abstractmethod
    def enable(self):
        pass
    
    @abstractmethod
    def disable(self):
        pass
    
    @abstractmethod
    def get_volume(self) -> int:
        pass
    
    @abstractmethod
    def set_volume(self, percent: int):
        pass

# Конкретные реализации
class TV(Device):
    def __init__(self):
        self.enabled = False
        self.volume = 20
    
    def is_enabled(self) -> bool:
        return self.enabled
    
    def enable(self):
        self.enabled = True
        print("TV включен")
    
    def disable(self):
        self.enabled = False
        print("TV выключен")
    
    def get_volume(self) -> int:
        return self.volume
    
    def set_volume(self, percent: int):
        if 0 <= percent <= 100:
            self.volume = percent
            print(f"Громкость TV установлена на {percent}%")
        else:
            print("Некорректная громкость")

class Radio(Device):
    def __init__(self):
        self.enabled = False
        self.volume = 30
    
    def is_enabled(self) -> bool:
        return self.enabled
    
    def enable(self):
        self.enabled = True
        print("Radio включен")
    
    def disable(self):
        self.enabled = False
        print("Radio выключен")
    
    def get_volume(self) -> int:
        return self.volume
    
    def set_volume(self, percent: int):
        if 0 <= percent <= 100:
            self.volume = percent
            print(f"Громкость Radio установлена на {percent}%")
        else:
            print("Некорректная громкость")

# Абстракция
class RemoteControl(ABC):
    def __init__(self, device: Device):
        self.device = device
    
    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()
    
    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)
    
    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

# Расширенная абстракция
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)
        print("Звук отключен")
