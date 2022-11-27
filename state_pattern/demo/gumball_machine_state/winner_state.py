from state import State

class WinnerState(State):
    def __init__(self, gumball_machine)-> None:
        self.gumball_machine = gumball_machine

    def insert_quarter(self):
        print("Please wait, we're already giving you a gumball")

    def eject_quarter(self):
        print("Sorry, you already turned the crank")

    def turn_cranck(self):
        print("Turning twice doesn't get you another gumball")

    def dispense(self):
        self.gumball_machine.release_ball()

        if self.gumball_machine._get_count() == 0:
            self.gumball_machine.set_state(self.gumball_machine._get_sold_out_state())
        else:
            self.gumball_machine.release_ball()
            print("YOU'RE A WINNER! You got two gumballs for your quarter")
            if self.gumball_machine._get_count() > 0:
                self.gumball_machine.set_state(self.gumball_machine._get_no_quarter_state())
            else:
                print("Oops, out of gumballs!")
                self.gumball_machine.set_state(self.gumball_machine._get_sold_out_state())