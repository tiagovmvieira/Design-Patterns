from model import Model
from view import View

from typing import Union

class Controller:
    def __init__(self)-> None:
        self.model: Model = Model()
        self.view: View = View(self)
  
    def main(self):
        self.view.main()

    def on_button_click(self, caption: Union[str, int]):
        result = self.model.calculate(caption)

        self.view.value_variable.set(result)

if __name__ == '__main__':
    calculator = Controller()
    calculator.main()