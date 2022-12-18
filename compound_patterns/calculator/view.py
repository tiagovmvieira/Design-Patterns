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
        self.value_variable = tk.StringVar(self)

        self._create_main_frame()
        self._create_entry()
        self._create_buttons()
        self._center_window()

    def main(self)-> None:
        self.mainloop()

    def _create_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)

    def _create_entry(self):
        ent = ttk.Entry(
            self.main_frame,
            justify="right",
            textvariable=self.value_variable,
            state=['readonly'])

        ent.pack(fill='x') # fill entire horizontal dimension

    def _create_buttons(self):
        outer_frame = ttk.Frame(self.main_frame)
        outer_frame.pack()

        inner_frame = ttk.Frame(outer_frame)
        inner_frame.pack()

        buttons_in_row = 0

        for caption in self.button_captions:
            if buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                inner_frame = ttk.Frame(outer_frame)
                inner_frame.pack()

                buttons_in_row = 0

            button = ttk.Button(
                inner_frame,
                text=caption,
                command=(lambda button=caption: self.controller.on_button_click(button))
                )
            button.pack(side="left")

            buttons_in_row += 1

    def _center_window(self):
        self.update()

        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenmmwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )