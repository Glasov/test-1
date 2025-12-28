from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        print("Windows Button")

class WindowsCheckbox(Checkbox):
    def paint(self):
        print("Windows Checkbox")

class MacButton(Button):
    def paint(self):
        print("Mac Button")

class MacCheckbox(Checkbox):
    def paint(self):
        print("Mac Checkbox")

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

    def render(self):
        self.button.paint()
        self.checkbox.paint()

if __name__ == '__main__':
    # проверяем, что каждая фабрика создаёт согласованные объекты
    apps = [Application(WindowsFactory()), Application(MacFactory())]

    for app in apps:
        app.render()