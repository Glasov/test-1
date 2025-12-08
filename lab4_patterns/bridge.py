class Device:
    def print_data(self, data):
        raise NotImplementedError

class Monitor(Device):
    def print_data(self, data):
        print(f"[Monitor] Показ на мониторе: {data}")

class Printer(Device):
    def print_data(self, data):
        print(f"[Printer] Печать на бумагу: {data}")

class Output:
    def __init__(self, device):
        self._device = device

    def render(self, data):
        raise NotImplementedError

class TextOutput(Output):
    def render(self, data):
        self._device.print_data(f"Текст: {data}")

class ImageOutput(Output):
    def render(self, data):
        self._device.print_data(f"Изображение (данные): {data}")

if __name__ == "__main__":
    print("=== BRIDGE ===")
    monitor = Monitor()
    printer = Printer()

    text_on_monitor = TextOutput(monitor)
    text_on_printer = TextOutput(printer)

    text_on_monitor.render("Hello, world!")
    text_on_printer.render("Hello, world!")

    image_on_monitor = ImageOutput(monitor)
    image_on_monitor.render("101010101")