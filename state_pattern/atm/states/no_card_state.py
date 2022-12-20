from states.atm_state import ATMState

class NoCardState(ATMState):
    def __init__(self, atm_machine):

        from atm_machine import ATMMachine
        self._atm_machine: ATMMachine = atm_machine

    def insert_card(self)-> None:
        print("Please Enter a PIN")
        self._atm_machine.set_atm_state(self._atm_machine._get_has_card_state())

    def eject_card(self)-> None:
        print("Enter a card first")

    def insert_pin(self, pin_entered: int)-> None:
        print("Enter a card first")

    def request_cash(self, cash_to_withdraw: int)-> None:
        print("Enter a card first")