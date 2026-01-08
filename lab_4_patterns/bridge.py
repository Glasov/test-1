class Device:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass
    
    def set_volume(self, level):
        pass


class TV(Device):
    def turn_on(self):
        return "TV turned on"
    
    def turn_off(self):
        return "TV turned off"
    
    def set_volume(self, level):
        return f"TV volume: {level}"


class Radio(Device):
    def turn_on(self):
        return "Radio turned on"
    
    def turn_off(self):
        return "Radio turned off"
    
    def set_volume(self, level):
        return f"Radio volumn: {level}"


class Remote:
    def __init__(self, device):
        self.device = device
    
    def power_on(self):
        return self.device.turn_on()
    
    def power_off(self):
        return self.device.turn_off()
    
    def volume_up(self):
        return self.device.set_volume(10)
    
    def volume_down(self):
        return self.device.set_volume(5)


class AdvancedRemote(Remote):
    def mute(self):
        return self.device.set_volume(0)

tv = TV()
radio = Radio()

basic_remote = Remote(tv)
print(basic_remote.power_on())
print(basic_remote.volume_up())

advanced_remote = AdvancedRemote(radio)
print(advanced_remote.power_on())
print(advanced_remote.mute())
