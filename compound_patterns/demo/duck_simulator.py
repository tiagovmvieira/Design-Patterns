from decorator.quack_counter import QuackCounter
from quackable import Quackable

from ducks.goose_duck import GooseDuck

from adapter.goose_adapter import GooseDuckAdapter

from factory.abstract_duck_factory import AbstractDuckFactory

class DuckSimulator:
    def __init__(self)-> None:
        pass

    def simulate(self, duck_factory: AbstractDuckFactory, duck: Quackable = None)-> None:
        if duck is None and duck_factory is not None:
            self.duck_factory = duck_factory

            self.mallard_duck: Quackable = self.duck_factory.create_mallard_duck()
            self.red_head_duck: Quackable = self.duck_factory.create_red_head_duck()
            self.duck_call: Quackable = self.duck_factory.create_duck_call()
            self.rubber_duck: Quackable = self.duck_factory.create_rubber_duck()
            self.goose_duck: Quackable = GooseDuckAdapter(GooseDuck())

            print("\nDuck Simulator")
            duck_factory=None
            self.simulate(duck_factory, self.mallard_duck)
            self.simulate(duck_factory, self.red_head_duck)
            self.simulate(duck_factory, self.duck_call)
            self.simulate(duck_factory, self.rubber_duck)
            self.simulate(duck_factory, self.goose_duck)

            print("The ducks quacked " + str(QuackCounter.get_quacks()) + " times")
        else:
            duck.quack()