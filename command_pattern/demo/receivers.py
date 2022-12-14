class Light:
    def __init__(self, location: str)-> None:
        self.location = location

    def on(self)-> None:
        print(f"{self.location.upper()}: The Light is on!")

    def off(self)-> None:
        print(f"{self.location.upper()}: The Light is off!")

class GarageDoor:
    def __init__(self, location: str)-> None:
        self.location = location

    def up(self)-> None:
        print(f"{self.location.upper()}: The door is up!")

    def down(self)-> None:
        print(f"{self.location.upper()}: The door is down!")

    def stop(self)-> None:
        print(f"{self.location.upper()}: The door is stoped!")

    def light_on(self)-> None:
        print(f"{self.location.upper()}: The Garage Light is on!")

    def light_off(self)-> None:
        print(f"{self.location.upper()}: The Garage Light is off!")

class Stereo:
    def __init__(self, location: str)-> None:
        self.location = location

    def on(self)-> None:
        print(f"{self.location.upper()}: The stereo is on!")

    def off(self)-> None:
        print(f"{self.location.upper()}: The stereo is off!")

    def set_CD(self)-> None:
        print(f"{self.location.upper()}: The stereo is set for CD input")

    def set_DVD(self)-> None:
        print(f"{self.location.upper()}: The stereo is set for DVD input")

    def set_radio(self)-> None:
        print(f"{self.location.upper()}: The stereo is set for Radio")

    def set_volume(self, value: int)-> None:
        print(f"{self.location.upper()}: Stereo volume set to {value}")

class TV:
    def __init__(self, location: str)-> None:
        self.location = location

    def on(self)-> None:
        print(f"{self.location.upper()}: The TV is on!")
    
    def off(self)-> None:
        print(f"{self.location.upper()}: The TV is off!")

    def set_input_channel(self, input_channel: int)-> None:
        self.input_channel = input_channel
        print(f"{self.location.upper()}: TV channel is set for DVD")

    def set_volume(self, value: int)-> None:
        print(f"{self.location.upper()}: TV volume set to {value}")

class CeilingFan:
    def __init__(self, location: str)-> None:
        self.location = location
        self.speed_map = {
            "HIGH": 3,
            "MEDIUM": 2,
            "LOW": 1,
            "OFF": 0
        }
        self.speed: int = self.speed_map.get("OFF")

    def high(self)-> None:
        self.speed = self.speed_map.get("HIGH")
        print(f"{self.location.upper()}: The ceiling fan is on high speed")

    def medium(self)-> None:
        self.speed = self.speed_map.get("MEDIUM")
        print(f"{self.location.upper()}: The ceiling fan is on medium speed")

    def low(self)-> None:
        self.speed = self.speed_map.get("LOW")
        print(f"{self.location.upper()}: The ceiling fan is on low speed")

    def off(self)-> None:
        self.speed = self.speed_map.get("OFF")
        print(f"{self.location.upper()}: The ceiling fan is off!")

    def get_speed(self)-> int:
        return self.speed

class Hottub:
    def __init__(self, location: str)-> None:
        self.location = location
        self.is_on: bool = False
        self.temperature: int = 0

    def on(self):
        self.is_on = True

    def off(self):
        self.is_on = False

    def circulate(self)-> None:
        if self.on:
            print(f"{self.location.upper()}: Hottub is bubbling!")

    def jets_on(self)-> None:
        if self.on:
            print(f"{self.location.upper()}: Hottub jets are on")

    def jets_off(self)-> None:
        if self.on:
            print(f"{self.location.upper()}: Hottub jets are off")

    def set_temperature(self, value: int)-> None:
        if value > self.temperature:
            print(f"{self.location.upper()}: Hottub is heating to a steaming {value} degrees")
        elif value < self.temperature:
            print(f"{self.location.upper()}: Hottub is cooling to {value} degrees")
        else:
            print(f"{self.location.upper()}: Nothing happens. Hottub is already at {value} degrees")
        self.temperature = value

class PartyMode:
    def __init__(self)-> None:
        pass

class KitchenLight:
    def __init__(self):
        pass

class LivingRoomLight:
    def __init__(self):
        pass

class LivingRoomCellingFan:
    def __init__(self):
        pass

class AllLights:
    def __init__(self):
        pass