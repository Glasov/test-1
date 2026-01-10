"""
Паттерн Цепочка обязанностей (Chain of Responsibility)
Позволяет передавать запрос по цепочке обработчиков.
"""

from abc import ABC, abstractmethod

# Базовый обработчик
class Logger(ABC):
    def __init__(self):
        self.next_logger = None
    
    def set_next(self, logger: 'Logger') -> 'Logger':
        self.next_logger = logger
        return logger
    
    @abstractmethod
    def log(self, message: str, level: str) -> str:
        pass
    
    def _next(self, message: str, level: str) -> str:
        if self.next_logger:
            return self.next_logger.log(message, level)
        return ""

# Конкретные обработчики
class ConsoleLogger(Logger):
    def log(self, message: str, level: str) -> str:
        if level == "INFO":
            result = f"[INFO] {message}"
            print(result)
            return result
        elif self.next_logger:
            return self._next(message, level)
        return ""

class FileLogger(Logger):
    def log(self, message: str, level: str) -> str:
        if level == "WARNING":
            result = f"[WARNING] {message} (записано в файл)"
            print(result)
            return result
        elif self.next_logger:
            return self._next(message, level)
        return ""

class EmailLogger(Logger):
    def log(self, message: str, level: str) -> str:
        if level == "ERROR":
            result = f"[ERROR] {message} (отправлено на email)"
            print(result)
            return result
        elif self.next_logger:
            return self._next(message, level)
        return ""

# Клиентский код
class Application:
    def __init__(self):
        # Создаем цепочку: Console -> File -> Email
        self.logger_chain = ConsoleLogger()
        self.logger_chain.set_next(FileLogger()).set_next(EmailLogger())
    
    def process_event(self, message: str, level: str):
        return self.logger_chain.log(message, level)
