from interfaces.fly_behaviour import FlyBehaviour

class FlyRocketPowered(FlyBehaviour):
    def __init__(self)-> None:
        pass

    def fly(self)-> str:
        return 'I am flying with a rocket'