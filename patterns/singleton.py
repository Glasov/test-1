class Logger:
    _logger = None

    def __new__(cls):
        if not cls._logger:
            cls._logger = super().__new__(cls)
            cls._logger.messages = []
        return cls._logger
    
    def add_message(self, text) :
        self.messages.append(text)
        print(f"Add log: {text} ")

    def show_log(self):
        return self.messages

logger1 = Logger()
logger1.add_message("First message")

logger2 = Logger()
logger2.add_message("Second message")

print(f"One and only logger: {logger1 is logger2}")
print(f"All messages: {logger1.show_log()}")
