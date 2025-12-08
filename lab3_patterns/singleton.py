class DatabaseConnection:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Создание нового подключения к базе данных...")
            cls._instance = super().__new__(cls)
            cls._instance.connection_string = "postgresql://localhost:5432/mydb"
        return cls._instance

    def query(self, sql):
        return f"Выполнение запроса '{sql}' через {self.connection_string}"


if __name__ == "__main__":

    db1 = DatabaseConnection()
    print(f"db1 ID: {id(db1)}")
    print(db1.query("SELECT * FROM users") + "\n")


    db2 = DatabaseConnection()
    print(f"db2 ID: {id(db2)}")
    print(db2.query("INSERT INTO users VALUES (1, 'John')") + "\n")

    # Проверка, что это один и тот же объект
    print(f"db1 и db2 - это один объект?: {db1 is db2}")