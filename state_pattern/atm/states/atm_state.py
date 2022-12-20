from abc import ABC, abstractmethod

class ATMState(ABC):
    @abstractmethod
    def insert_card(self)-> None:
        pass

    @abstractmethod
    def eject_card(self)-> None:
        pass

    @abstractmethod
    def insert_pin(self, pin_entered: int)-> None:
        pass

    @abstractmethod
    def request_cash(self, cash_to_withdraw: int)-> None:
        pass