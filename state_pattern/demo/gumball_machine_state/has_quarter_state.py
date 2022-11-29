import random
from state import State

class HasQuarterState(State):
    def __init__(self, gumball_machine):
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("You can't insert another quarter")

    def eject_quarter(self):
        print("Quarter returned")
        self.gumball_machine.set_state(self.gumball_machine._get_no_quarter_state())

    def turn_cranck(self):
        print("You turned...")
        winner = random.randrange(10)
        if winner == 0 and self.gumball_machine._get_count() > 1:
            self.gumball_machine.set_state(self.gumball_machine._get_winner_state())
        else:
            self.gumball_machine.set_state(self.gumball_machine._get_sold_state())

    def dispense(self):
        print("You need need to turn the crank")
