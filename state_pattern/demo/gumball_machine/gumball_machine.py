from typing import Final

class GumballMachine:
    _SOLD_OUT: Final[int] = 0
    _NO_QUARTER: Final[int] = 1
    _HAS_QUARTER: Final[int] = 2
    _SOLD: Final[int] = 3

    _state: int = _SOLD_OUT

    def __init__(self, count: int)-> None:
        self.count = count
        self._state = None
        if self.count > 0:
            self._state: int = GumballMachine._NO_QUARTER

    def __str__(self)-> str:
        return f"Mighty Gumball, Inc.\n" + "Python-enabled Standing Gumball Model #2022\n" + f"Inventory: {self.count} gumballs\n" +\
                "Machine is waiting for quarter"

    def insert_quarter(self)-> None:
        if self._state == GumballMachine._HAS_QUARTER:
            print("You can't insert another quarter")
        elif self._state == GumballMachine._NO_QUARTER:
            self._state = GumballMachine._HAS_QUARTER
            print("You inserted a quarter")
        elif self._state == GumballMachine._SOLD_OUT:
            print("You can't insert a quarter, the machine is sold out")
        elif self._state == GumballMachine._SOLD:
            print("Please wait, we're already giving you a gumball")

    def eject_quarter(self)-> None:
        if self._state == GumballMachine._HAS_QUARTER:
            print("Quarter returned")
            self._state = GumballMachine._NO_QUARTER
        elif self._state == GumballMachine._NO_QUARTER:
            print("You haven't inserted a quarter")
        elif self._state == GumballMachine._SOLD_OUT:
            print("You can't eject, you haven't inserted a quarter yet")
        elif self._state == GumballMachine._SOLD:
            print("Sorry, you already turned the crank")

    def turn_cranck(self)-> None:
        if self._state == GumballMachine._HAS_QUARTER:
            print("You turned...")
            self._state = GumballMachine._SOLD
        elif self._state == GumballMachine._NO_QUARTER:
            print("you turned but there's no quarter")
        elif self._state == GumballMachine._SOLD_OUT:
            print("You turned . but there are no gumballs")
        elif self._state == GumballMachine._SOLD:
            print("Turning twice doesn't get you another gumball")

    def dispense(self)-> None:
        if self._state == GumballMachine._SOLD:
            print("A gumball comes rolling out the slot")
            self.count += -1
            if self.count == 0:
                print("Oops, out of gumballs!")
                self._state = GumballMachine._SOLD_OUT
            else:
                self._state = GumballMachine._NO_QUARTER
        elif self._state == GumballMachine._NO_QUARTER:
            print("You need to pay first")
        elif self._state == GumballMachine._SOLD_OUT:
            print("No gumball dispensed")
        elif self._state == GumballMachine._HAS_QUARTER:
            print("You need to turn the crank")
