from states.atm_state import ATMState

class HasCorrectPinState(ATMState):
    def __init__(self, atm_machine)-> None:

        from atm_machine import ATMMachine
        self._atm_machine: ATMMachine = atm_machine

    def insert_card(self)-> None:
        print("You can't enter more than one card")
    
    def eject_card(self)-> None:
        print("Card ejected")
        self._atm_machine.set_atm_state(self._atm_machine._get_no_card_state())

    def insert_pin(self, pin_entered: int)-> None:
        print("Already entered a PIN")

    def request_cash(self, cash_to_withdraw: int)-> None:
        if cash_to_withdraw > self._atm_machine._cash_in_machine:
            print("Don't have that cash")
            print("Card Ejected")
            self._atm_machine.set_atm_state(self._atm_machine._get_no_card_state())
        else:
            print(f"{cash_to_withdraw} is provided by the machine")
            self._atm_machine.set_cash_in_machine(self._atm_machine._cash_in_machine - cash_to_withdraw)

            print("Card Ejected")
            self._atm_machine.set_atm_state(self._atm_machine._get_no_card_state())

            if self._atm_machine._cash_in_machine <= 0:
                self._atm_machine.set_atm_state(self._atm_machine._get_out_of_money_state())