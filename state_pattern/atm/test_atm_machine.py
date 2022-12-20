from atm_machine import ATMMachine
from termcolor import colored

class TestATMMachine:
    def __init__(self)-> None:
        self.atm_machine = ATMMachine()
        print(colored('-------------------- INSERT CARD --------------------', 'red'))
        self.atm_machine.insert_card()

        print(colored('-------------------- EJECT CARD ---------------------', 'blue'))
        self.atm_machine.eject_card()

        print(colored('-------------------- INSERT CARD --------------------', 'red'))
        self.atm_machine.insert_card()

        print(colored('-------------------- INSERT PIN ---------------------', 'green'))
        self.atm_machine.insert_pin(1234)

        print(colored('------------------- REQUEST CASH --------------------', 'yellow'))
        self.atm_machine.request_cash(2000)

        print(colored('-------------------- INSERT CARD --------------------', 'red'))
        self.atm_machine.insert_card()

        print(colored('-------------------- INSERT PIN ---------------------', 'green'))
        self.atm_machine.insert_pin(1234)


if __name__ == '__main__':
    print(colored('-------------------- STATE PATTERN ------------------', 'white'))
    atm_machine = TestATMMachine()