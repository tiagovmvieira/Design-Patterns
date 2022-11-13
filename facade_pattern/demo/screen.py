import inspect

class Screen:
    def __init__(self):
        pass

    def up(self)-> str:
        print(f"Theater {self.__class__.__name__} going {inspect.stack()[0][3]}")

    def down(self)-> str:
        print(f"Theater {self.__class__.__name__} going {inspect.stack()[0][3]}")