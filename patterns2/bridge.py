cat > bridge.py << 'EOF'
class Device:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

class TV(Device):
    def turn_on(self):
        return "TV включен"
    
    def turn_off(self):
        return "TV выключен"

class Radio(Device):
    def turn_on(self):
        return "Radio включен"
    
    def turn_off(self):
        return "Radio выключен"

class Remote:
    def __init__(self, device):
        self.device = device
    
    def toggle_power(self):
        pass

class BasicRemote(Remote):
    def toggle_power(self):
        return self.device.turn_on()

# Пример
if __name__ == "__main__":
    tv = TV()
    remote = BasicRemote(tv)
    print(remote.toggle_power())
EOF