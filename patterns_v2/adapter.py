class EuropeanSocket:
    def voltage(self):
        return 220
    
    def live(self):
        return "Phase (220V)"

    def neutral(self):
        return "Neutral"
    
    def earth(self):
        return "Earth"


class USPlug:
    def voltage(self):
        return 110
    
    def hot(self):
        return "Phase (110V)"
    
    def neutral(self):
        return "Neutral"


class USPlugAdapter:
    def __init__(self, us_plug):    
        self.us_plug = us_plug
    
    def voltage(self):
        return self.us_plug.voltage()
    
    def live(self):
        return self.us_plug.hot()
    
    def neutral(self):
        return self.us_plug.neutral()
    
    def earth(self):
        return "Adapter: without grounding"

european_socket = EuropeanSocket()
print("European socket:")
print(f" Voltage: {european_socket.voltage()}V")
print(f" Contacts: {european_socket.live()}, {european_socket.neutral()}, {european_socket.earth()}")

us_plug = USPlug()
adapter = USPlugAdapter(us_plug)

print("\nAmerican plug via adapter:")
print(f" Voltage: {adapter.voltage()}V")
print(f" Contacts: {adapter.live()}, {adapter.neutral()}, {adapter.earth()}")
