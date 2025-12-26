from abc import ABC, abstractmethod

class ExternalLogger:
    def log_message(self, msg):
        print(f"External log: {msg}")

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class LoggerAdapter(Logger):
    def __init__(self, external_logger: ExternalLogger):
        self.external_logger = external_logger

    def log(self, message):
        self.external_logger.log_message(message)

if __name__ == '__main__':
    # проверяем, что адаптер позволяет использовать несовместимый интерфейс как нужный
    external_logger = ExternalLogger()
    logger = LoggerAdapter(external_logger)
    logger.log("This is a test message")
