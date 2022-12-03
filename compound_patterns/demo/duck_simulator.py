from ducks.mallard_duck import MallardDuck
from ducks.red_head_duck import RedHeadDuck
from ducks.duck_call import DuckCall
from ducks.rubber_duck import RubberDuck
from ducks.goose_duck import GooseDuck

from quackable import Quackable
from goose_adapter import GooseDuckAdapter

class DuckSimulator:
    def __init__(self)-> None:
        pass

    def simulate(self, duck: Quackable = None):
        if duck is None:
            self.mallard_duck: Quackable = MallardDuck()
            self.red_head_duck: Quackable = RedHeadDuck()
            self.duck_call: Quackable = DuckCall()
            self.rubber_duck: Quackable = RubberDuck()
            self.goose_duck: Quackable = GooseDuckAdapter(GooseDuck())

            print("\nDuck Simulator")
            self.simulate(self.mallard_duck)
            self.simulate(self.red_head_duck)
            self.simulate(self.duck_call)
            self.simulate(self.rubber_duck)
            self.simulate(self.goose_duck)
        else:
            duck.quack()