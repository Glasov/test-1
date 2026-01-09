from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self): pass

class WinButton(Button):
    def paint(self): return "Windows button"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self): pass

class WinFactory(GUIFactory):
    def create_button(self): return WinButton()
