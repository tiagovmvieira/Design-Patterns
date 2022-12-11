from observer.quack_observable import QuackObservable

from abc import ABC, abstractmethod

class Quackable(QuackObservable, ABC):
    @abstractmethod
    def quack(self):
        pass
