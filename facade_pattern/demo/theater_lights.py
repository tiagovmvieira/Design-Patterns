import inspect

class TheaterLights:
    def __init__(self)-> None:
        pass

    def on(self)-> str:
        print(f"Theater Ceiling Lights {inspect.stack()[0][3]}")

    def off(self)-> str:
        return "Off"

    def dim(self, dim_value: int)-> str:
        print(f"Theater Ceiling Lights dimming to {dim_value}%")