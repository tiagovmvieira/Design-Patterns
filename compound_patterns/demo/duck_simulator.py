from decorator.quack_counter import QuackCounter
from quackable import Quackable

from ducks.goose_duck import GooseDuck

from adapter.goose_adapter import GooseDuckAdapter

from factory.abstract_duck_factory import AbstractDuckFactory 
from factory.goose_duck_factory import GooseDuckFactory
from composite.flock import Flock

class DuckSimulator:
    def __init__(self)-> None:
        pass

    def simulate(self, duck_factory: AbstractDuckFactory, goose_duck_factory: GooseDuckFactory, duck: Quackable = None)-> None:
        if duck is None and duck_factory is not None and goose_duck_factory is not None:
            self.duck_factory = duck_factory
            self.goose_duck_factory = goose_duck_factory

            # self.mallard_duck: Quackable = self.duck_factory.create_mallard_duck()
            self.red_head_duck: Quackable = self.duck_factory.create_red_head_duck()
            self.duck_call: Quackable = self.duck_factory.create_duck_call()
            self.rubber_duck: Quackable = self.duck_factory.create_rubber_duck()
            self.goose_duck: Quackable = self.goose_duck_factory.create_goose_duck()

            # print("\nDuck Simulator")
            print("Duck Simulator: With Composite - Flocks")

            flock_of_ducks = Flock()
            flock_of_ducks.add(self.red_head_duck)
            flock_of_ducks.add(self.duck_call)
            flock_of_ducks.add(self.rubber_duck)
            flock_of_ducks.add(self.goose_duck)

            flock_of_mallards = Flock()
            self.mallard_one: Quackable = self.duck_factory.create_mallard_duck()
            self.mallard_two: Quackable = self.duck_factory.create_mallard_duck()
            self.mallard_three: Quackable = self.duck_factory.create_mallard_duck()
            self.mallard_four: Quackable = self.duck_factory.create_mallard_duck()
            flock_of_mallards.add(self.mallard_one)
            flock_of_mallards.add(self.mallard_two)
            flock_of_mallards.add(self.mallard_three)
            flock_of_mallards.add(self.mallard_four)

            flock_of_ducks.add(flock_of_mallards)

            duck_factory=None
            goose_duck_factory = None

            print("\nDuck Simulator: Whole Flock Simulation")
            self.simulate(duck_factory, goose_duck_factory, flock_of_ducks)

            print("\nDuck Simulator: Mallard Flock Simulation")
            self.simulate(duck_factory, goose_duck_factory, flock_of_mallards)

            # self.simulate(duck_factory, goose_duck_factory, self.mallard_duck)
            # self.simulate(duck_factory, goose_duck_factory, self.red_head_duck)
            # self.simulate(duck_factory, goose_duck_factory, self.duck_call)
            # self.simulate(duck_factory, goose_duck_factory, self.rubber_duck)
            # self.simulate(duck_factory, goose_duck_factory, self.goose_duck)

            print("\nThe ducks quacked " + str(QuackCounter.get_quacks()) + " times")
        else:
            duck.quack()