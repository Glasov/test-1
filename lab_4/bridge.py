from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def print(self, data):
        pass

class Monitor(Device):
    def print(self, data):
        print(f"Displaying on monitor: {data}")

class Printer(Device):
    def print(self, data):
        print(f"Printing to paper: {data}")

class Output(ABC):
    def __init__(self, device: Device):
        self.device = device

    @abstractmethod
    def render(self, data):
        pass

class TextOutput(Output):
    def render(self, data):
        self.device.print("Text: " + data)

class ImageOutput(Output):
    def render(self, data):
        self.device.print("Image: [Binary data: " + data + "]")

if __name__ == '__main__':
    # проверяем независимость абстракции и реализации
    monitor = Monitor()
    printer = Printer()

    text_monitor = TextOutput(monitor)
    text_printer = TextOutput(printer)

    text_monitor.render("Hello, world!")
    text_printer.render("Hello, world!")

    image_monitor = ImageOutput(monitor)
    image_monitor.render("101010101")