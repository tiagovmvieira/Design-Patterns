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

    def deposit_cash(self, cash_to_deposit: int)-> None:
        if cash_to_deposit > 0:
            print(f"{cash_to_deposit} is deposited on the machine")
            self._atm_machine.set_cash_in_machine(self._atm_machine._cash_in_machine + cash_to_deposit)

            print("Card Ejected")            
        else:
            print("Error. Card Ejected")

        self._atm_machine.set_atm_state(self._atm_machine._get_has_card_state())