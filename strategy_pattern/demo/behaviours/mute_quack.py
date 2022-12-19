from interfaces.quack_behaviour import QuackBehaviour

class MuteQuack(QuackBehaviour):
    def __init__(self)-> None:
        pass

    def quack(self)-> str:
        return "I can't quack"