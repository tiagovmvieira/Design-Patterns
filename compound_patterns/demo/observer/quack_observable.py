from abc import ABC, abstractmethod

class QuackObservable(ABC):
    @abstractmethod
    def register_observer(self, observer)-> None:
        pass

    @abstractmethod
    def notify_observers(self, observer)-> None:
        pass