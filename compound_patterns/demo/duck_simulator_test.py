from duck_simulator import DuckSimulator
from factory.counting_duck_factory import CountingDuckFactory

from termcolor import colored

if __name__ == '__main__':
    print(colored('------------------ COMPOUND PATTERNS ----------------', 'white'))
    duck_simulator = DuckSimulator()
    duck_factory = CountingDuckFactory()
    duck_simulator.simulate(duck_factory)