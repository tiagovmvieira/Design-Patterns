from duck_simulator import DuckSimulator
from factory.counting_duck_factory import CountingDuckFactory
from factory.goose_duck_factory import GooseDuckFactory

from termcolor import colored

if __name__ == '__main__':
    print(colored('------------------ COMPOUND PATTERNS ----------------', 'white'))
    print(colored('---------------- SIMPLE DUCK SIMULATOR --------------', 'blue'))
    duck_simulator = DuckSimulator()
    duck_simulator.simulate(initial=True)

    print(colored('---------------- USING A DUCK ADAPTER ---------------', 'red'))
    duck_simulator.simulate(adapter=True)

    print(colored('------------ USING A QUACKABLE DECORATOR ------------', 'green'))
    duck_simulator.simulate(decorator=True, adapter=True)

    print(colored('------------- USING ABSTRACT FACTORIES --------------', 'yellow'))
    duck_factory = CountingDuckFactory()
    goose_duck_factory = GooseDuckFactory()
    duck_simulator.simulate(duck_factory=duck_factory, goose_duck_factory=goose_duck_factory)

    print(colored('------------- USING FLOCKS COMPOSITES ---------------', 'cyan'))
    duck_simulator.simulate(duck_factory=duck_factory, goose_duck_factory=goose_duck_factory, composite=True)

    print(colored('---------- USING A QUACKOLOGIST OBSERVER ------------', 'magenta'))
    duck_simulator.simulate(duck_factory=duck_factory, goose_duck_factory=goose_duck_factory, composite=True, observer=True)