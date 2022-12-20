from states.atm_state import ATMState
from states.has_card_state import HasCardState
from states.no_card_state import NoCardState
from states.has_correct_pin_state import HasCorrectPinState
from states.out_of_money_state import OutOfMoneyState

from typing import Final

class ATMMachine:
    _cash_in_machine: int = 2000

    def __init__(self)-> None:
        self.has_card: Final[ATMState] = HasCardState(self)
        self.no_card: Final[ATMState] = NoCardState(self)
        self.has_correct_pin: Final[ATMState] = HasCorrectPinState(self)
        self.out_of_money: Final[ATMState] = OutOfMoneyState(self)

        self._atm_state: Final[ATMState] = self.no_card

        self.correct_pin_entered: bool = False

        if self._cash_in_machine < 0:
            self._atm_state = self.out_of_money

    def set_atm_state(self, new_atm_state: ATMState)-> None:
        self._atm_state = new_atm_state

    @classmethod
    def set_cash_in_machine(cls, new_cash_in_machine: int)-> None:
        cls._cash_in_machine = new_cash_in_machine

    def insert_card(self)-> None:
        self._atm_state.insert_card()

    def eject_card(self)-> None:
        self._atm_state.eject_card()

    def request_cash(self, cash_to_withdraw: int)-> None:
        self._atm_state.request_cash(cash_to_withdraw)

    def deposit_cash(self, cash_to_deposit: int)-> None:
        self._atm_state.deposit_cash(cash_to_deposit)

    def insert_pin(self, pin_entered: int)-> None:
        self._atm_state.insert_pin(pin_entered)

    def _get_current_state(self)-> ATMState:
        return self._atm_state

    def _get_has_card_state(self)-> ATMState:
        return self.has_card

    def _get_no_card_state(self)-> ATMState:
        return self.no_card

    def _get_has_correct_pin_state(self)-> ATMState:
        return self.has_correct_pin

    def _get_out_of_money_state(self)-> ATMState:
        return self.out_of_money