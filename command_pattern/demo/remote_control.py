from commands import *

class SimpleRemoteControl:
    def __init__(self, no_of_slots: int, no_command: NoCommand = NoCommand())-> None:
        self.no_of_slots = no_of_slots
        self.on_commands: list = [no_command] * self.no_of_slots
        self.off_commands: list = [no_command] * self.no_of_slots
        self.undo_command : Command = no_command

    def __str__(self):
        string_buffer: list = []
        string_buffer.append("\n------------- Remote Control --------------\n")

        for i in range(self.no_of_slots):
            on_command = self.on_commands[i].__class__.__name__
            off_command = self.on_commands[i].__class__.__name__
            string_buffer.append("[slot " + str(i) + "] " + on_command + "    " + off_command + "\n")

        return " ".join(str(e) for e in string_buffer)

    def set_command(self, slot_index: int, on_command: Command, off_command: Command)-> None:
        self.on_commands[slot_index] = on_command
        self.off_commands[slot_index] = off_command

    def on_button_was_pressed(self, slot_index: int):
        self.on_commands[slot_index].execute()
        self.undo_command = self.on_commands[slot_index]

    def off_button_was_pressed(self, slot_index: int):
        self.off_commands[slot_index].execute()
        self.undo_command = self.off_commands[slot_index]

    def undo_button_was_pressed(self):
        self.undo_command.undo()