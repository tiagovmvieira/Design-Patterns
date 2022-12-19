from ducks.duck import Duck
from interfaces.fly_behaviour import FlyBehaviour
from interfaces.quack_behaviour import QuackBehaviour

class RedHeadDuck(Duck):
    def __init__(self, fly_behaviour: FlyBehaviour, quack_behaviour: QuackBehaviour):
        super().__init__(fly_behaviour, quack_behaviour)

    def display(self)-> str:
        return "Looks like a Red Head!"