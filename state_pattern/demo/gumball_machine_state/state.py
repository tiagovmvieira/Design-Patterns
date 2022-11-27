from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_cranck(self):
        pass

    @abstractmethod
    def dispense(self):
        pass