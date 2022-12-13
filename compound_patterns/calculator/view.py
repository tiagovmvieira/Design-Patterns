import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    PAD = 10

    MAX_BUTTONS_PER_ROW = 4
    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self, controller)-> None:
        super().__init__()

        from controller import Controller
        self.controller: Controller = controller

        self.title("PyCalc")
        self.value_variable = tk.StringVar(self, "Hello World")

        self._create_main_frame()
        self._create_entry()
        self._create_buttons()

    def main(self)-> None:
        self.mainloop()

    def _create_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx= self.PAD, pady = self.PAD)

    def _create_entry(self):
        ent = ttk.Entry(self.main_frame, justify='right', textvariable=self.value_variable)
        ent.pack() 

    def _create_buttons(self):
        frame = ttk.Frame(self.main_frame)
        frame.pack()

        for caption in self.button_captions:
            button = ttk.Button(frame, text=caption)
            button.pack()