from states.atm_state import ATMState

class OutOfMoneyState(ATMState):
    def __init__(self, atm_machine)-> None:

        from atm_machine import ATMMachine
        self._atm_machine: ATMMachine = atm_machine

    def insert_card(self)-> None:
        print("We don't have money")

    def eject_card(self)-> None:
        print("We don't have money. You did not enter a card")

    def insert_pin(self, pin_entered: int)-> None:
        print("We don't have money")

    def request_cash(self, cash_to_withdraw: int)-> None:
        print("We don't have money")