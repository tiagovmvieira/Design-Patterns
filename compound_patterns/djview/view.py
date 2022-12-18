import tkinter as tk
from tkinter import ttk

class DJView(tk.Tk):
    PAD = 100
    DROPDOWN_OPTIONS = [
        "Start",
        "Stop",
        "Quit"
    ]

    def __init__(self, controller)-> None:
        super().__init__()

        from controller import Controller
        self.controller: Controller = controller
        self.title('Control')

        self.option_variable = tk.StringVar(self)
        self.bpm_variable = tk.StringVar(self)

        self._create_view()
        
    def _create_view(self):
        self._create_main_frame()
        self._create_bpm_labels()
        self._create_set_button()
        self._create_decrease_bpm_button()
        # self._create_option_menu()

    def main(self)-> None:
        self.mainloop()

    def _create_main_frame(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=self.PAD, pady=self.PAD)

    def _create_bpm_labels(self):
        enter_bpm_frame = ttk.Frame(self.main_frame)
        enter_bpm_frame.pack()

        enter_bpm_caption = tk.Label(
            enter_bpm_frame,
            textvariable='Enter BPM:',
            foreground='white'
        )

        enter_bpm_label = tk.Label(
            enter_bpm_frame,
            textvariable=self.bpm_variable,
            background='white'    
        )

        enter_bpm_caption.pack(side='left')
        enter_bpm_label.pack(side='right', fill='x')

    def _create_set_button(self)-> None:
        set_button_frame = ttk.Frame(self.main_frame)
        set_button_frame.pack()

        set_button = ttk.Button(
            set_button_frame,
            text='Set',
            command=(lambda :self.controller.set_bpm())
        )

        set_button.pack()

    def _create_decrease_bpm_button(self)-> None:
        bpm_management_button_frame = ttk.Frame(self.main_frame)
        bpm_management_button_frame.pack()

        decrease_bpm_button = ttk.Button(
            bpm_management_button_frame,
            text='<<',
            command=(lambda :self.controller.decrease_bpm())
        )

        increase_bpm_button = ttk.Button(
            bpm_management_button_frame,
            text='>>',
            command=(lambda :self.controller.increase_bpm())
        )
        
        decrease_bpm_button.pack(side='left')
        increase_bpm_button.pack(side='right')

    def _create_option_menu(self):
        self.option_variable.set('DJ Control')
        option_menu = tk.OptionMenu(
            self.main_frame,
            self.option_variable,
            *self.DROPDOWN_OPTIONS
        )
        option_menu.pack()

    def _create_label(self):
        label = tk.Label(
            self.main_frame,
            textvariable=self.bpm_variable,
            background='white'
            )

        label.pack()
