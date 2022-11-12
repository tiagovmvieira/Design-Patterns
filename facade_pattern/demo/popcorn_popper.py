import inspect

class PopcornPopper:
    def __init__(self)-> None:
        pass

    def on(self)-> str:
        print(f"{self.__class__.__name__} {inspect.stack()[0][3]}")

    def off(self)-> str:
        print(f"{self.__class__.__name__} {inspect.stack()[0][3]}")

    def pop(self)-> str:
        print(f"{self.__class__.__name__} popping popcorn!")