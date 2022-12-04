from duck_simulator import DuckSimulator
from factory.counting_duck_factory import CountingDuckFactory
from factory.goose_duck_factory import GooseDuckFactory

from termcolor import colored

if __name__ == '__main__':
    print(colored('------------------ COMPOUND PATTERNS ----------------', 'white'))
    duck_simulator = DuckSimulator()
    duck_factory = CountingDuckFactory()
    goose_duck_factory = GooseDuckFactory()
    duck_simulator.simulate(duck_factory, goose_duck_factory)