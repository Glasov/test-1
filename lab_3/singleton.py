class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.value = 0
        return cls._instance

if __name__ == '__main__':
    a = Singleton()
    b = Singleton()

    # проверяем, что оба объекта — один и тот же экземпляр
    print(a is b)

    # проверяем глобальный доступ
    a.value = 1
    print(b.value)