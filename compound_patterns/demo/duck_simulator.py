from decorator.quack_counter import QuackCounter
from quackable import Quackable

from ducks.goose_duck import GooseDuck
from ducks.mallard_duck import MallardDuck
from ducks.red_head_duck import RedHeadDuck
from ducks.duck_call import DuckCall
from ducks.rubber_duck import RubberDuck

from adapter.goose_adapter import GooseDuckAdapter

from factory.abstract_duck_factory import AbstractDuckFactory 
from factory.goose_duck_factory import GooseDuckFactory
from composite.flock import Flock
from observer.quackologist import Quackologist

class DuckSimulator:
    def __init__(self)-> None:
        pass

    def simulate(self, initial: bool = False, duck: Quackable = None, adapter: bool = False, decorator: bool = False,\
            duck_factory: AbstractDuckFactory = None, goose_duck_factory: GooseDuckFactory = None, composite: bool = False,\
            observer: bool = False)-> None:

        if initial or adapter:
            if decorator:
                self.mallard_duck: Quackable = QuackCounter(MallardDuck())
                self.red_head_duck: Quackable = QuackCounter(RedHeadDuck())
                self.duck_call: Quackable = QuackCounter(DuckCall())
                self.rubber_duck: Quackable = QuackCounter(RubberDuck())
            else:
                self.mallard_duck: Quackable = MallardDuck()
                self.red_head_duck: Quackable = RedHeadDuck()
                self.duck_call: Quackable = DuckCall()
                self.rubber_duck: Quackable = RubberDuck()

            if adapter:
                self.goose_duck: Quackable = GooseDuckAdapter(GooseDuck())

            if decorator:
                print("\nDuck Simulator: With Decorator")
            else:
                print("\nDuck Simulator")

            self.simulate(duck=self.mallard_duck)
            self.simulate(duck=self.red_head_duck)
            self.simulate(duck=self.duck_call)
            self.simulate(duck=self.rubber_duck)

            if adapter:
                self.simulate(duck=self.goose_duck)

            if decorator:
                print("\nThe ducks quacked " + str(QuackCounter.get_quacks()) + " times")

        elif duck is None and duck_factory and goose_duck_factory:
            QuackCounter.reset_number_of_quacks()
            self.duck_factory = duck_factory
            self.goose_duck_factory = goose_duck_factory

            self.mallard_duck: Quackable = self.duck_factory.create_mallard_duck()
            self.red_head_duck: Quackable = self.duck_factory.create_red_head_duck()
            self.duck_call: Quackable = self.duck_factory.create_duck_call()
            self.rubber_duck: Quackable = self.duck_factory.create_rubber_duck()
            self.goose_duck: Quackable = self.goose_duck_factory.create_goose_duck()

            if composite:
                print("\nDuck Simulator: With Composite - Flocks")

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

                if observer:
                    QuackCounter.reset_number_of_quacks()
                    print("\nDuck Simulator: With Observer")
                    quackologist = Quackologist()
                    flock_of_ducks.register_observer(quackologist)

                    self.simulate(duck=flock_of_ducks, duck_factory=duck_factory, goose_duck_factory=goose_duck_factory)
                else:
                    print("\nDuck Simulator: Whole Flock Simulation")
                    self.simulate(duck=flock_of_ducks, duck_factory=duck_factory, goose_duck_factory=goose_duck_factory)

                    print("\nDuck Simulator: Mallard Flock Simulation")
                    self.simulate(duck= flock_of_mallards, duck_factory=duck_factory, goose_duck_factory=goose_duck_factory)
            else:
                print("\nDuck Simulator: With Abstract Factory")
                duck_factory=None
                goose_duck_factory = None
                self.simulate(duck=self.mallard_duck, duck_factory=duck_factory, goose_duck_factory=goose_duck_factory)
                self.simulate(duck=self.red_head_duck, duck_factory=duck_factory, goose_duck_factory=goose_duck_factory)
                self.simulate(duck=self.duck_call, duck_factory=duck_factory, goose_duck_factory=goose_duck_factory)
                self.simulate(duck=self.rubber_duck, duck_factory=duck_factory, goose_duck_factory=goose_duck_factory)
                self.simulate(duck=self.goose_duck, duck_factory=duck_factory, goose_duck_factory=goose_duck_factory)

            print("\nThe ducks quacked " + str(QuackCounter.get_quacks()) + " times")
        else:
            duck.quack()