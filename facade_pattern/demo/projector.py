import inspect

class Projector:
    def __init__(self):
        pass

    def on(self):
        print(f"{self.__class__.__name__} {inspect.stack()[0][3]}")

    def off(self):
        print(f"{self.__class__.__name__} {inspect.stack()[0][3]}")

    def wide_screen_mode(self):
        print(f"{self.__class__.__name__} in widescreen mode (16:9 aspect ratio)")