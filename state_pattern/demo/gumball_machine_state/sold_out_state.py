from state import State

class SoldOutState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert a quarter, the machine is sold out")

    def eject_quarter(self):
        print("You can't eject, you haven't inserted a quarter yet")

    def turn_cranck(self):
        print("You turned, but there are no gumballs")

    def dispense(self):
        print("No gumball dispensed")