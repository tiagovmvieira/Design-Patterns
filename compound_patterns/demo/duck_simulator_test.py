from duck_simulator import DuckSimulator
from termcolor import colored

if __name__ == '__main__':
    print(colored('------------------ COMPOUND PATTERNS ----------------', 'white'))
    duck_simulator = DuckSimulator()
    duck_simulator.simulate()