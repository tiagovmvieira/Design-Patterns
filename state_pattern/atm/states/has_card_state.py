from states.atm_state import ATMState

class HasCardState(ATMState):
    def __init__(self, atm_machine)-> None:

        from atm_machine import ATMMachine
        self._atm_machine: ATMMachine = atm_machine

    def insert_card(self)-> None:
        print("You can't enter more than one card")

    def eject_card(self)-> None:
        print("Card ejected")
        self._atm_machine.set_atm_state(self._atm_machine._get_no_card_state())

    def insert_pin(self, pin_entered: int)-> None:
        if pin_entered == 1234:
            print("Correct PIN")
            self._atm_machine.correct_pin_entered = True
            self._atm_machine.set_atm_state(self._atm_machine._get_has_correct_pin_state())
        else:
            print("Wrong PIN")
            self._atm_machine.correct_pin_entered = False
            print("Card Ejected")
            self._atm_machine.set_atm_state(self._get_no_card_state())

    def request_cash(self, cash_to_withdraw: int)-> None:
        print("Enter PIN first!")

    def deposit_cash(self, cash_to_deposit: int) -> None:
        print("Enter PIN first!")