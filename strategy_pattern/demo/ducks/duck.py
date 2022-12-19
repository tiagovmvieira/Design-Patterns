from interfaces.fly_behaviour import FlyBehaviour
from interfaces.quack_behaviour import QuackBehaviour

class Duck():
    def __init__(self, fly_behaviour: FlyBehaviour, quack_behaviour: QuackBehaviour):
        self.fly_behaviour = fly_behaviour
        self.quack_behaviour = quack_behaviour

    def display(self)-> str:
        pass

    def swim(self)-> str:
        return 'All ducks float, even decoys!'

    def set_fly_behaviour(self, fly_behaviour: FlyBehaviour):
        self.fly_behaviour = fly_behaviour

    def set_quack_behaviour(self, quack_behaviour: QuackBehaviour):
        self.quack_behaviour = quack_behaviour

    def perform_quack(self)-> str:
        return self.quack_behaviour.quack(self)

    def perform_fly(self)-> str:
        return self.fly_behaviour.fly(self)