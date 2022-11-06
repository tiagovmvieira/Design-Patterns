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