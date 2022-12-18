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
        self.config(background="#000078")
        self._configure_button_styles()
        self.value_variable = tk.StringVar(self)

        self._create_main_frame()
        self._create_label()
        self._create_buttons()
        self._center_window()

    def _configure_button_styles(self)-> None:
        style = ttk.Style()
        style.theme_use('default')

        # style used on number buttons
        style.configure(
            'N.TButton',
            foreground='white',
            background='#29e7d6',
            font=('Arial', 20)
        )

        # style used on operator buttons
        style.configure(
            'O.TButton',
            foreground='white',
            background='#00003E',
            font=('Arial', 20)
        )

        # style used on miscellaneous buttons
        style.configure(
            'M.TButton',
            foreground='white',
            background='#b2b4b6',
            font=('Arial', 20)
        )

    def main(self)-> None:
        self.mainloop()

    def _create_main_frame(self)-> None:
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)

    def _create_label(self)-> None:
        label = tk.Label(
            self.main_frame,
            anchor='e',
            textvariable=self.value_variable,
            background='#00003E',
            foreground='white',
            font=('Arial', 30)
            )

        label.pack(fill='x') # fill entire horizontal dimension

    def _create_buttons(self)-> None:
        outer_frame = ttk.Frame(self.main_frame)
        outer_frame.pack()

        is_first_row = True
        buttons_in_row = 0

        for caption in self.button_captions:
            if is_first_row or buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                is_first_row = False

                inner_frame = ttk.Frame(outer_frame)
                inner_frame.pack(fill='x')

                buttons_in_row = 0
            
            if isinstance(caption, int):
                style_prefix= 'N'
            elif self._is_operator(caption):
                style_prefix= 'O'
            else:
                style_prefix= 'M'

            style_name = f'{style_prefix}.TButton'

            button = ttk.Button(
                inner_frame,
                text=caption,
                command=(lambda button=caption: self.controller.on_button_click(button)),
                style=style_name
                )

            if caption == 0:
                fill = 'x'
                expand = 1
            else:
                fill = 'none',
                expand = 0

            button.pack(fill=fill, expand=expand, side="left")

            buttons_in_row += 1

    def _is_operator(self, button_caption: str)-> bool:
        return button_caption in ['/', '*', '-', '+', '=']

    def _center_window(self)-> None:
        self.update()

        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenmmwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )