from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class ConsoleLogger(Logger):
    def log(self, message: str):
        print("Logging to console:", message)

class FileLogger(Logger):
    def log(self, message: str):
        print("Logging to file:", message)

class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

    def process(self, message: str):
        logger = self.create_logger()
        print("Created logger type:", type(logger).__name__)
        logger.log(message)

class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()

class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()

if __name__ == '__main__':
    # проверяем, что каждая фабрика создаёт нужный тип логгера
    factories = [ConsoleLoggerFactory(), FileLoggerFactory()]

    for factory in factories:
        factory.process("Test message")