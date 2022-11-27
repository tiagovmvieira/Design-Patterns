from state import State
from sold_out_state import SoldOutState
from no_quarter_state import NoQuarterState
from has_quarter_state import HasQuarterState
from sold_state import SoldState
from winner_state import WinnerState

from typing import Final

class GumballMachineState:
    def __init__(self, number_of_gumballs: int)-> None:
        self.sold_out_state: Final[State] = SoldOutState(self)
        self.no_quarter_state: Final[State] = NoQuarterState(self)
        self.has_quarter_state: Final[State] = HasQuarterState(self)
        self.sold_state: Final[State] = SoldState(self)
        self.winner_state: Final[State] = WinnerState(self)

        self._count = number_of_gumballs
        if number_of_gumballs > 0:
            self._state = self.no_quarter_state
        else:
            self._state = self.sold_out_state

    def __str__(self)-> str:
        return f"Mighty Gumball, Inc.\n" + "Python-enabled Standing Gumball Model #2022\n" + f"Inventory: {self._count} gumball(s) \n" +\
                f"Machine is {self._state.__class__.__name__}\n"

    def insert_quarter(self)-> None:
        self._state.insert_quarter()

    def eject_quarter(self)-> None:
        self._state.eject_quarter()

    def turn_crank(self)-> None:
        self._state.turn_cranck()
        self._state.dispense()

    def set_state(self, state: State)-> None:
        self._state = state

    def release_ball(self)-> None:
        print("A gumball comes rolling out the slot")
        if self._count > 0:
            self._count += -1

    def _get_state(self)-> State:
        return self._state

    def _get_sold_out_state(self)-> State:
        return self.sold_out_state

    def _get_no_quarter_state(self)-> State:
        return self.no_quarter_state

    def _get_has_quarter_state(self)-> State:
        return self.has_quarter_state

    def _get_sold_state(self)-> State:
        return self.sold_state

    def _get_winner_state(self)-> State:
        return self.winner_state

    def _get_count(self)-> int:
        return self._count