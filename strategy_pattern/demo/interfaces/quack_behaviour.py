from abc import ABC, abstractmethod

class QuackBehaviour(ABC):
    @abstractmethod
    def quack(self):
        pass