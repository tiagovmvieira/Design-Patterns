from __future__ import annotations
from abc import ABC, abstractmethod

from receivers import *

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass 

class MacroComand(Command):
    def __init__(self, commands: list):
        self.commands = commands

    def execute(self):
        for i in range(len(self.commands)):
            self.commands[i].execute()

    def undo(self):
        for i in range(len(self.commands)):
            self.commands[i].undo()

class NoCommand(Command):
    def __init__(self)-> None:
        pass

    def execute(self)-> None:
        pass

    def undo(self)-> None:
        pass

class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

class StereoOnCommand(Command):
    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()

    def undo(self):
        self.stereo.off()

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

    def undo(self):
        self.stereo.on()

class GarageDoorOpenCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()

    def undo(self):
        self.garage_door.down()

class GarageDoorCloseCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()

    def undo(self):
        self.garage_door.up()

class GarageDoorStopCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.stop()

class GarageDoorLightOnCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.light_on()

    def undo(self):
        self.garage_door.light_off()

class GarageDoorLightOffCommand(Command):
    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.light_off()

    def undo(self):
        self.garage_door.light_on()

class TVOnCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.on()
        self.tv.set_input_channel(3)

    def undo(self):
        self.tv.off()

class TVOffCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.off()
    
    def undo(self):
        self.tv.on()

class CeilingFanOnCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan
        self.previous_speed: int = 0

    def execute(self):
        self.previous_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()

    def undo(self):
        if self.previous_speed == 3:
            self.ceiling_fan.high()
        elif self.previous_speed == 2:
            self.ceiling_fan.medium()
        elif self.previous_speed == 1:
            self.ceiling_fan.low()
        elif self.previous_speed == 0:
            self.ceiling_fan.off()

class CeilingFanHighCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan
        self.previous_speed: int = 0

    def execute(self):
        self.previous_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()

    def undo(self):
        if self.previous_speed == 3:
            self.ceiling_fan.high()
        elif self.previous_speed == 2:
            self.ceiling_fan.medium()
        elif self.previous_speed == 1:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()

class CeilingFanMediumCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan
        self.previous_speed: int = 0

    def execute(self):
        self.previous_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.medium()

    def undo(self):
        if self.previous_speed == 3:
            self.ceiling_fan.high()
        elif self.previous_speed == 2:
            self.ceiling_fan.medium()
        elif self.previous_speed == 1:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()

class CeilingFanLowCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan
        self.previous_speed: int = 0

    def execute(self):
        self.previous_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.low()

    def undo(self):
        if self.previous_speed == 3:
            self.ceiling_fan.high()
        elif self.previous_speed == 2:
            self.ceiling_fan.medium()
        elif self.previous_speed == 1:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()

class CeilingFanOffCommand(Command):
    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan
        self.previous_speed: int = 0

    def execute(self):
        self.previous_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.off()

    def undo(self):
        if self.previous_speed == 3:
            self.ceiling_fan.high()
        elif self.previous_speed == 2:
            self.ceiling_fan.medium()
        elif self.previous_speed == 1:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()