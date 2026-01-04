from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

class WindowsButton(Button):
    def click(self):
        return "Windows кнопка нажата"

class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows чекбокс отмечен"

class MacButton(Button):
    def click(self):
        return "Mac кнопка нажата"

class MacCheckbox(Checkbox):
    def check(self):
        return "Mac чекбокс отмечен"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()
    
    def paint(self):
        return f"{self.button.click()}, {self.checkbox.check()}"
