from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "{ Windows Button }"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "{ Windows Checkbox }"

class MacButton(Button):
    def render(self):
        return "[ macOS Button ]"

class MacCheckbox(Checkbox):
    def render(self):
        return "[ macOS Checkbox ]"

# Конкретные продукты для Linux
class LinuxButton(Button):
    def render(self):
        return "{ Linux Button }"

class LinuxCheckbox(Checkbox):
    def render(self):
        return "{ Linux Checkbox }"


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

class LinuxFactory(GUIFactory):
    def create_button(self) -> Button:
        return LinuxButton()
    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()

class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render(self):
        return f"{self.button.render()}\n{self.checkbox.render()}"

if __name__ == "__main__":
    print("Создание GUI для Windows:")
    app_windows = Application(WindowsFactory())
    print(app_windows.render() + "\n")

    print("Создание GUI для macOS:")
    app_mac = Application(MacFactory())
    print(app_mac.render() + "\n")

    print("Создание GUI для Linux:")
    app_linux = Application(LinuxFactory())
    print(app_linux.render())