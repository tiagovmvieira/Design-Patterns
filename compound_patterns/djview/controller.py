from interfaces.controller_interface import ControllerInterface
from view import DJView
from model import Model

class Controller(ControllerInterface):
    def __init__(self)-> None:
        self.model: Model = Model()
        self.view: DJView = DJView(self)

    def start(self)-> None:
        pass

    def stop(self)-> None:
        pass

    def increase_bpm(self) -> None:
        print('I am here')

    def decrease_bpm(self)-> None:
        print('I am here')

    def set_bpm(self)-> None:
        print('I am here')
        pass

    def main(self)-> None:
        self.view.main()

if __name__ == '__main__':
    dj_view = Controller()
    dj_view.main()