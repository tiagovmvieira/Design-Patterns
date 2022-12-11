from observer.quack_observable import QuackObservable

from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, duck: QuackObservable)-> None:
        pass