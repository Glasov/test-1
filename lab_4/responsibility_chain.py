from abc import ABC, abstractmethod
from enum import Enum

class RequestType(Enum):
    TYPE_A = 1
    TYPE_B = 2

class Request:
    def __init__(self, type_: RequestType):
        self.type = type_

class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    @abstractmethod
    def handle(self, request: Request):
        pass

class ConcreteHandlerA(Handler):
    def handle(self, request: Request):
        if request.type == RequestType.TYPE_A:
            print("ConcreteHandlerA handled the request")
        elif self.next_handler:
            self.next_handler.handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request: Request):
        if request.type == RequestType.TYPE_B:
            print("ConcreteHandlerB handled the request")
        elif self.next_handler:
            self.next_handler.handle(request)

if __name__ == '__main__':
    # проверяем, что запросы проходят по цепочке
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_a.set_next(handler_b)

    handler_a.handle(Request(RequestType.TYPE_A))
    handler_a.handle(Request(RequestType.TYPE_B))
