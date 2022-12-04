from ..quackable import Quackable

class DecoyDuck(Quackable):
    def __init__(self):
        pass

    def quack(self)-> None:
        print("Silence")