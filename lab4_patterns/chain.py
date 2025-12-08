class Request:
    """Простой запрос с типом и сообщением."""
    def __init__(self, request_type, message):
        self.request_type = request_type
        self.message = message

class Handler:
    """Базовый обработчик в цепочке."""
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, request):
        if self._next:
            self._next.handle(request)

class AuthHandler(Handler):
    def handle(self, request):
        if request.request_type == "auth":
            print(f"[AuthHandler] Обрабатываю запрос аутентификации: {request.message}")
        else:
            print("[AuthHandler] Не мой тип, передаю дальше...")
            super().handle(request)

class LogHandler(Handler):
    def handle(self, request):
        if request.request_type == "log":
            print(f"[LogHandler] Логирую событие: {request.message}")
        else:
            print("[LogHandler] Не мой тип, передаю дальше...")
            super().handle(request)

class ErrorHandler(Handler):
    def handle(self, request):
        if request.request_type == "error":
            print(f"[ErrorHandler] Обрабатываю ошибку: {request.message}")
        else:
            print("[ErrorHandler] Конец цепочки, обработчика нет.")

if __name__ == "__main__":
    print("=== CHAIN OF RESPONSIBILITY ===")
    auth = AuthHandler()
    log = LogHandler()
    error = ErrorHandler()

    # Строим цепочку: auth -> log -> error
    auth.set_next(log).set_next(error)

    auth.handle(Request("auth", "Логин пользователя"))
    auth.handle(Request("log", "Пользователь открыл страницу профиля"))
    auth.handle(Request("error", "Не удалось сохранить данные"))
    auth.handle(Request("unknown", "Какой-то странный запрос"))
    print()