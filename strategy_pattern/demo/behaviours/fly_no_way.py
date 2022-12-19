from interfaces.fly_behaviour import FlyBehaviour

class FlyNoWay(FlyBehaviour):
    def __init__(self)-> None:
        pass

    def fly(self)-> str:
        return "I can't fly"