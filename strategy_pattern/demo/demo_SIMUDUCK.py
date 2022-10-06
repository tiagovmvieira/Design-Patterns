from __future__ import annotations
from abc import ABC, abstractmethod
from termcolor import colored

class Duck():
    def __init__(self, fly_behaviour: FlyBehaviour, quack_behaviour: QuackBehaviour):
        self.fly_behaviour = fly_behaviour
        self.quack_behaviour = quack_behaviour

    def display()-> str:
        pass

    def swim(self)-> str:
        return 'All ducks float, even decoys!'

    def set_fly_behaviour(self, fly_behaviour: FlyBehaviour):
        self.fly_behaviour = fly_behaviour

    def set_quack_behaviour(self, quack_behaviour: QuackBehaviour):
        self.quack_behaviour = quack_behaviour
    
    def perform_quack(self):
        return self.quack_behaviour.quack(self)

    def perform_fly(self):
        return self.fly_behaviour.fly(self)

class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehaviour):
    def __init__(self):
        pass

    def fly(self):
        return 'I am flying'

class FlyRocketPowered(FlyBehaviour):
    def __init__(self):
        pass

    def fly(self):
        return 'I am flying with a rocket'

class FlyNoWay(FlyBehaviour):
    def __init__(self):
        pass

    def fly(self):
        return "I can't fly"

# quack behaviour interface
class QuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBehaviour):
    def __init__(self):
        pass

    def quack(self):
        return 'I am duck quacking'

class Squeak(QuackBehaviour):
    def __init__(self):
        pass

    def quack(self):
        return 'I am rubber duckie squeaking'

class MuteQuack(QuackBehaviour):
    def __init__(self):
        pass

    def quack(self):
        return "I can't quack"

class MallardDuck(Duck):
    def __init__(self, fly_behaviour, quack_behaviour):
        super().__init__(fly_behaviour, quack_behaviour)

    def display(self)-> str:
        return 'Looks like a Mallard!'

class RedHeadDuck(Duck):
    def __init__(self, fly_behaviour, quack_behaviour):
        super().__init__(fly_behaviour, quack_behaviour)

    def display(self)-> str:
        return 'Looks like a Red Head!'

class RubberDuck(Duck):
    def __init__(self, fly_behaviour, quack_behaviour):
        super().__init__(fly_behaviour, quack_behaviour)

    def display(self)-> str:
        return 'Looks like a Rubber Duck!'

class DecoyDuck(Duck):
    def __init__(self, fly_behaviour, quack_behaviour):
        super().__init__(fly_behaviour, quack_behaviour)

    def display(self)-> str:
        return 'Looks like a Decoy Duck!'

if __name__ == '__main__':
    print(colored('-------------------- MALLARD DUCK -------------------', 'red'))
    mallard_duck = MallardDuck(FlyWithWings, Quack)
    print(mallard_duck.display())
    print(mallard_duck.swim())
    print(mallard_duck.perform_fly())
    mallard_duck.set_fly_behaviour(FlyRocketPowered)
    print(mallard_duck.perform_fly())
    print(mallard_duck.perform_quack())

    print(colored('------------------- RED HEAD DUCK -------------------', 'blue'))
    red_head_duck = RedHeadDuck(FlyWithWings,Quack)
    print(red_head_duck.display())
    print(red_head_duck.swim())
    red_head_duck.set_fly_behaviour(FlyNoWay)
    print(red_head_duck.perform_fly())
    print(red_head_duck.perform_quack())

    print(colored('-------------------- RUBBER DUCK --------------------', 'green'))
    rubber_duck = RubberDuck(FlyNoWay, Squeak)
    print(rubber_duck.display())
    print(rubber_duck.swim())
    rubber_duck.set_fly_behaviour(FlyRocketPowered)
    print(rubber_duck.perform_fly())
    print(rubber_duck.perform_quack())

    print(colored('-------------------- DECOY DUCK ---------------------', 'yellow'))
    decoy_duck = DecoyDuck(FlyNoWay, MuteQuack)
    print(decoy_duck.display())
    print(decoy_duck.swim())
    print(decoy_duck.perform_fly())
    print(decoy_duck.perform_quack())