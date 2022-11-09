from termcolor import colored

from receivers import *
from commands import *
from remote_control import *

if __name__ == '__main__':
    print(colored('------------------ COMMAND PATTERN ------------------', 'white'))
    print(colored('------------- SIMPLE REMOTE CONTROL TEST ------------', 'blue'))
    simple_remote_control = SimpleRemoteControl()
    
    light = Light('living room')
    light_on_command = LightOnCommand(light)

    garage_door = GarageDoor('garage')
    garage_door_open_command = GarageDoorOpenCommand(garage_door)

    simple_remote_control.set_command(light_on_command)
    simple_remote_control.button_was_pressed()

    simple_remote_control.set_command(garage_door_open_command)
    simple_remote_control.button_was_pressed()

    print(colored('\n---------------- REMOTE CONTROL TEST ----------------', 'red'))
    remote_control = RemoteControl(7)

    living_room_light = Light('living room')
    kitchen_light = Light('kitchen')
    ceiling_fan = CeilingFan('living room')
    garage_door = GarageDoor('garage')
    stereo = Stereo('living room')

    living_room_light_on_command = LightOnCommand(living_room_light)
    living_room_light_off_command = LightOffCommand(living_room_light)
    kitchen_light_light_on_command = LightOnCommand(kitchen_light)
    kitchen_light_light_off_command = LightOffCommand(kitchen_light)

    ceiling_fan_on_command = CeilingFanOnCommand(ceiling_fan)
    ceiling_fan_off_command = CeilingFanOffCommand(ceiling_fan)

    garage_door_open_command = GarageDoorOpenCommand(garage_door)
    garage_door_close_command = GarageDoorCloseCommand(garage_door)

    stereo_on_with_CD_command = StereoOnWithCDCommand(stereo)
    stereo_off_command = StereoOffCommand(stereo)

    remote_control.set_command(0, living_room_light_on_command, living_room_light_off_command)
    remote_control.set_command(1, kitchen_light_light_on_command, kitchen_light_light_off_command)
    remote_control.set_command(2, ceiling_fan_on_command, ceiling_fan_off_command)
    remote_control.set_command(3, stereo_on_with_CD_command, stereo_off_command)

    print(remote_control, '\n')

    remote_control.on_button_was_pressed(0)
    remote_control.off_button_was_pressed(0)
    remote_control.on_button_was_pressed(1)
    remote_control.off_button_was_pressed(1)
    remote_control.on_button_was_pressed(2)
    remote_control.off_button_was_pressed(2)
    remote_control.on_button_was_pressed(3)
    remote_control.off_button_was_pressed(3)

    print(colored('\n---------- REMOTE WITH MACRO COMMAND TEST -----------', 'green'))
    macro_command_remote_control = RemoteControl(4)

    living_room_light = Light('living room')
    living_room_tv = TV('living room')
    stereo = Stereo('living room')
    hot_tub = Hottub('bathroom')

    light_on_command = LightOnCommand(living_room_light)
    tv_on_command = TVOnCommand(living_room_tv)
    stereo_on_command = StereoOnCommand(stereo)
    hot_tub_on_command = HottubOnCommand(hot_tub)

    light_off_command = LightOffCommand(living_room_light)
    tv_off_command = TVOffCommand(living_room_tv)
    stereo_off_command = StereoOffCommand(stereo)
    hot_tub_off_command = HottubOffCommand(hot_tub)

    party_on = (light_on_command, stereo_on_command, tv_on_command, hot_tub_on_command)
    party_off = (light_off_command, stereo_off_command, tv_off_command, hot_tub_off_command)

    party_on_macro = MacroComand(party_on)
    party_off_macro = MacroComand(party_off)

    macro_command_remote_control.set_command(0, party_on_macro, party_off_macro)

    macro_command_remote_control.on_button_was_pressed(0)
    macro_command_remote_control.off_button_was_pressed(0)
    print(macro_command_remote_control)