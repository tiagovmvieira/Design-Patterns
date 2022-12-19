from abc import ABC, abstractmethod

class FlyBehaviour(ABC):
    @abstractmethod
    def fly(self)-> None:
        pass