cat > adapter.py << 'EOF'
class EuropeanSocket:
    def voltage(self):
        return 220
    
    def plug(self):
        return "Европейская вилка"

class AmericanSocket:
    def voltage(self):
        return 110
    
    def plug_type(self):
        return "Американская вилка"

class Adapter:
    def __init__(self, socket):
        self.socket = socket
    
    def voltage(self):
        return self.socket.voltage()
    
    def plug(self):
        if hasattr(self.socket, 'plug_type'):
            return f"Адаптер для {self.socket.plug_type()}"
        return self.socket.plug()

# Пример
if __name__ == "__main__":
    eu_socket = EuropeanSocket()
    print(f"Европа: {eu_socket.voltage()}V, {eu_socket.plug()}")
    
    us_socket = AmericanSocket()
    adapter = Adapter(us_socket)
    print(f"США через адаптер: {adapter.voltage()}V, {adapter.plug()}")
EOF