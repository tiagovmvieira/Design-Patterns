from gumball_machine import GumballMachine

from termcolor import colored

if __name__ == '__main__':
    print(colored('-------------------- STATE PATTERN ------------------', 'white'))
    gumball_machine = GumballMachine(5)
    print(gumball_machine)
    
    gumball_machine.insert_quarter()
    gumball_machine.turn_cranck()