from gumball_machine_state import GumballMachineState

from termcolor import colored

if __name__ == '__main__':
    print(colored('-------------------- STATE PATTERN ------------------', 'white'))
    gumball_machine = GumballMachineState(5)
    print(colored(gumball_machine, 'blue'))

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    print('\n')
    print(colored(gumball_machine, 'blue'))

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    print('\n')
    print(colored(gumball_machine, 'blue'))