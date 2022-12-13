from model import Model
from view import View

class Controller:
    def __init__(self)-> None:
        self.model: Model = Model()
        self.view: View = View(self)
  
    def main(self):
        self.view.main()

if __name__ == '__main__':
    calculator = Controller()
    calculator.main()