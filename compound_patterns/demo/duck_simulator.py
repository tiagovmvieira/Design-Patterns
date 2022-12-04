from decorator.quack_counter import QuackCounter
from quackable import Quackable

from ducks.mallard_duck import MallardDuck
from ducks.red_head_duck import RedHeadDuck
from ducks.duck_call import DuckCall
from ducks.rubber_duck import RubberDuck
from ducks.goose_duck import GooseDuck

from adapter.goose_adapter import GooseDuckAdapter

class DuckSimulator:
    def __init__(self)-> None:
        pass

    def simulate(self, duck: Quackable = None):
        if duck is None:
            self.mallard_duck: Quackable = QuackCounter(MallardDuck())
            self.red_head_duck: Quackable = QuackCounter(RedHeadDuck())
            self.duck_call: Quackable = QuackCounter(DuckCall())
            self.rubber_duck: Quackable = QuackCounter(RubberDuck())
            self.goose_duck: Quackable = GooseDuckAdapter(GooseDuck())

            print("\nDuck Simulator")
            self.simulate(self.mallard_duck)
            self.simulate(self.red_head_duck)
            self.simulate(self.duck_call)
            self.simulate(self.rubber_duck)
            self.simulate(self.goose_duck)

            print("The ducks quacked " + str(QuackCounter.get_quacks()) + " times")
        else:
            duck.quack()