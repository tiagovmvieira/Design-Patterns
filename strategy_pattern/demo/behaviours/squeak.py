from interfaces.quack_behaviour import QuackBehaviour

class Squeak(QuackBehaviour):
    def __init__(self)-> None:
        pass

    def quack(self)-> str:
        return "I am rubber duckie squeaking"