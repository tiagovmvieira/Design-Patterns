from __future__ import annotations
from abc import ABC, abstractmethod
from termcolor import colored

from ducks import mallard_duck, decoy_duck, red_head_duck, rubber_duck, duck
from behaviours import fly_no_way, fly_rocket_powered, fly_with_wings, mute_quack, quack, squeak
from interfaces import fly_behaviour, quack_behaviour

class StrategyPatternTestDrive:
    def __init__(self)-> None:
        print(colored('-------------------- MALLARD DUCK -------------------', 'red'))
        self._test_mallard_duck()
        print(colored('------------------- RED HEAD DUCK -------------------', 'blue'))
        self._test_red_head_duck()
        print(colored('-------------------- RUBBER DUCK --------------------', 'green'))
        self._test_rubber_duck()
        print(colored('-------------------- DECOY DUCK ---------------------', 'yellow'))
        self._test_decoy_duck()

    def _test_mallard_duck(self)-> None:
        self.mallard_duck = mallard_duck.MallardDuck(fly_with_wings.FlyWithWings, quack.Quack)
        print(self.mallard_duck.display())
        print(self.mallard_duck.swim())
        print(self.mallard_duck.perform_fly())
        print(self.mallard_duck.perform_quack())

        self._set_duck_fly_behaviour(self.mallard_duck, fly_rocket_powered.FlyRocketPowered)
        
        print(self.mallard_duck.perform_fly())
        print(self.mallard_duck.perform_quack())

    def _test_red_head_duck(self)-> None:
        self.red_head_duck = red_head_duck.RedHeadDuck(fly_with_wings.FlyWithWings, quack.Quack)
        print(self.red_head_duck.display())
        print(self.red_head_duck.swim())
        print(self.red_head_duck.perform_fly())
        print(self.red_head_duck.perform_quack())

        self._set_duck_fly_behaviour(self.red_head_duck, fly_no_way.FlyNoWay)
        print(self.red_head_duck.perform_fly())
        print(self.red_head_duck.perform_quack())

    def _test_rubber_duck(self)-> None:
        self.rubber_duck = rubber_duck.RubberDuck(fly_no_way.FlyNoWay, squeak.Squeak)
        print(self.rubber_duck.display())
        print(self.rubber_duck.swim())
        print(self.rubber_duck.perform_fly())
        print(self.rubber_duck.perform_quack())

        self._set_duck_quack_behaviour(self.rubber_duck, mute_quack.MuteQuack)
        print(self.rubber_duck.perform_fly())
        print(self.rubber_duck.perform_quack())

    def _test_decoy_duck(self)-> None:
        self.decoy_duck = decoy_duck.DecoyDuck(fly_no_way.FlyNoWay, mute_quack.MuteQuack)
        print(self.decoy_duck.display())
        print(self.decoy_duck.swim())
        print(self.decoy_duck.perform_fly())
        print(self.decoy_duck.perform_quack())

        self._set_duck_fly_behaviour(self.decoy_duck, quack.Quack)

    @staticmethod
    def _set_duck_fly_behaviour(duck: duck.Duck, fly_behaviour: fly_behaviour.FlyBehaviour)-> None:
        duck.set_fly_behaviour(fly_behaviour)

    @staticmethod
    def _set_duck_quack_behaviour(duck: duck.Duck, quack_behaviour: quack_behaviour.QuackBehaviour)-> None:
        duck.set_quack_behaviour(quack_behaviour)

if __name__ == '__main__':
    print(colored('----------------- STRATEGY PATTERN ----------------', 'white'))
    strategy_pattern_test_drive = StrategyPatternTestDrive()