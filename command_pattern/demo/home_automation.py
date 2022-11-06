from termcolor import colored

from receivers import *
from commands import *
from remote_control import *

if __name__ == '__main__':
    print(colored('------------------ COMMAND PATTERN ------------------', 'white'))
    remote_control = SimpleRemoteControl(7)

    print(colored('----------------- LIVING ROOM LIGHT -----------------', 'blue'))
    living_room_light = Light('living room')
    living_room_light_on_command = LightOnCommand(living_room_light)
    living_room_light_off_command = LightOffCommand(living_room_light)
    remote_control.set_command(0, living_room_light_on_command, living_room_light_off_command)
    remote_control.on_button_was_pressed(0)
    remote_control.off_button_was_pressed(0)
    remote_control.undo_button_was_pressed()

    print(colored('------------------- KITCHEN LIGHT -------------------', 'red'))
    kitchen_light = Light('kitchen')
    kitchen_light_on_command = LightOnCommand(kitchen_light)
    kitchen_light_off_command = LightOffCommand(kitchen_light)
    remote_control.set_command(1, kitchen_light_on_command, kitchen_light_off_command)
    remote_control.on_button_was_pressed(1)
    remote_control.off_button_was_pressed(1)

    print(colored('-------------------- CEILING FAN --------------------', 'yellow'))
    ceiling_fan = CeilingFan('living room')
    ceiling_fan_on_command = CeilingFanOnCommand(ceiling_fan)
    ceiling_fan_high_command = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_medium_command = CeilingFanMediumCommand(ceiling_fan)
    ceiling_fan_off_command = CeilingFanOffCommand(ceiling_fan)
    remote_control.set_command(2, ceiling_fan_medium_command, ceiling_fan_off_command)
    remote_control.set_command(3, ceiling_fan_high_command, ceiling_fan_off_command)
    remote_control.on_button_was_pressed(2)
    remote_control.off_button_was_pressed(2)
    remote_control.undo_button_was_pressed()

    remote_control.on_button_was_pressed(3)
    remote_control.off_button_was_pressed(3)
    remote_control.undo_button_was_pressed()
    
    print(colored('-------------------- GARAGE DOOR --------------------', 'green'))
    garage_door = GarageDoor('garage')
    garage_door_open_command = GarageDoorOpenCommand(garage_door)
    garage_door_close_command = GarageDoorCloseCommand(garage_door)
    remote_control.set_command(4, garage_door_open_command, garage_door_close_command)
    remote_control.on_button_was_pressed(4)
    remote_control.off_button_was_pressed(4)

    print(colored('----------------------- STEREO ----------------------', 'cyan'))
    stereo = Stereo('living room')
    stereo_on_with_cd_command = StereoOnWithCDCommand(stereo)
    stereo_off_command = StereoOffCommand(stereo) 
    remote_control.set_command(5, stereo_on_with_cd_command, stereo_off_command)
    remote_control.on_button_was_pressed(5)
    remote_control.off_button_was_pressed(5)

    print(colored('------------------- REMOTE CONTROL ------------------', 'grey'))
    print(remote_control)