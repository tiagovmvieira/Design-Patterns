from __future__ import annotations
from abc import ABC, abstractmethod

from receivers import *

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    #@abstractmethod
    #def undo(self):
    #    pass 

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

class StereoOnCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()

class StereoOnWithCDCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_CD()
        self.stereo.set_volume(11)

class StereoOnWithDVDCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_DVD()
        self.stereo.set_volume(12)

class StereoOnWithRadioCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_radio()
        self.stereo.set_volume(10)

class StereoOffCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

class GarageDoorOpenCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()

class GarageDoorCloseCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()

class GarageDoorStopCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        return self.garage_door.stop()

class GarageDoorLightOnCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        return self.garage_door.light_on()

class GarageDoorLightOffCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        return self.garage_door.light_off()

class TVOnCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.on()
        self.tv.set_input_channel()

class TVOffCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.off()

class CeilingFanOnCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.ceiling_fan.high()

class CeilingFanHighCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.ceiling_fan.high()

class CeilingFanMediumCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.ceiling_fan.medium()

class CeilingFanLowCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.ceiling_fan.low()

class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.ceiling_fan.off()