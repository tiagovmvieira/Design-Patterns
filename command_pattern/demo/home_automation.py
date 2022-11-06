from abc import ABC, abstractmethod
from termcolor import colored
import sys

from receivers import *
from commands import *

class SimpleRemoteControl:
    def __init__(self, no_of_slots: int)-> None:
        self.no_of_slots = no_of_slots
        self.on_commands: list = [None] * self.no_of_slots
        self.off_commands: list = [None] * self.no_of_slots

    def __str__(self):
        string_buffer: list = []
        string_buffer.append("\n------------- Remote Control --------------\n")

        for i in range(self.no_of_slots):
            on_command = self.on_commands[i].__class__.__name__ if self.on_commands[i].__class__.__name__ != "NoneType" else "No Command"
            off_command = self.off_commands[i].__class__.__name__ if self.off_commands[i].__class__.__name__ != "NoneType" else "No Command"
            string_buffer.append("[slot " + str(i) + "] " + on_command + "    " + off_command + "\n")

        return " ".join(str(e) for e in string_buffer)

    def set_command(self, slot_index: int, on_command: Command, off_command: Command)-> None:
        self.on_commands[slot_index] = on_command
        self.off_commands[slot_index] = off_command

    def on_button_was_pressed(self, slot_index: int):
        self.on_commands[slot_index].execute()

    def off_button_was_pressed(self, slot_index: int):
        return self.off_commands[slot_index].execute()

if __name__ == '__main__':
    print(colored('------------------ COMMAND PATTERN ------------------', 'white'))
    remote_control = SimpleRemoteControl(7)

    living_room_light = Light('living room')
    kitchen_light = Light('kitchen')
    ceiling_fan = CeilingFan('living room')
    garage_door = GarageDoor('garage')
    stereo = Stereo('living room')

    living_room_light_on_command = LightOnCommand(living_room_light)
    living_room_light_off_command = LightOffCommand(living_room_light)

    kitchen_light_on_command = LightOnCommand(kitchen_light)
    kitchen_light_off_command = LightOffCommand(kitchen_light)

    ceiling_fan_on_command = CeilingFanOnCommand(ceiling_fan)
    ceiling_fan_off_command = CeilingFanOffCommand(ceiling_fan)

    garage_door_open_command = GarageDoorOpenCommand(garage_door)
    garage_door_close_command = GarageDoorCloseCommand(garage_door)

    stereo_on_with_cd_command = StereoOnWithCDCommand(stereo)
    stereo_off_command = StereoOffCommand(stereo) 

    remote_control.set_command(0, living_room_light_on_command, living_room_light_off_command)
    remote_control.set_command(1, kitchen_light_on_command, kitchen_light_off_command)
    remote_control.set_command(2, ceiling_fan_on_command, ceiling_fan_off_command)
    remote_control.set_command(3, garage_door_open_command, garage_door_close_command)
    remote_control.set_command(4, stereo_on_with_cd_command, stereo_off_command)

    print(remote_control)

    remote_control.on_button_was_pressed(0)
    remote_control.off_button_was_pressed(0)
    
    remote_control.on_button_was_pressed(1)
    remote_control.off_button_was_pressed(1)

    remote_control.on_button_was_pressed(2)
    remote_control.off_button_was_pressed(2)

    remote_control.on_button_was_pressed(3)
    remote_control.off_button_was_pressed(3)

    remote_control.on_button_was_pressed(4)
    remote_control.off_button_was_pressed(4)

    # print("Light on Command")
    # light = Light()
    # light_on_command = LightOnCommand(light)
    # light_off_command = LightOffCommand(light)
    # remote.set_command(0, light_on_command, light_off_command)
    # print(remote.on_button_was_pressed(0))
    # print(remote.off_button_was_pressed(0))
    # print("Garage on Command")
    # garage_door = GarageDoor()
    # garage_door_open_command = GarageDoorOpenCommand(garage_door)
    # remote.set_command(garage_door_open_command)
    # print(remote.button_was_pressed())