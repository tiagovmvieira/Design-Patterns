from quackable import Quackable
from observer.observer import Observer
from observer.observable import Observable

class RubberDuck(Quackable):
    def __init__(self)-> None:
        self.observable = Observable(self)

    def __str__(self)-> str:
        return "Rubber Duck"

    def notify_observers(self)-> None:
        self.observable.notify_observers()

    def quack(self)-> None:
        print("Squeak")
        self.notify_observers()
        
    def register_observer(self, observer: Observer)-> None:
        self.observable.register_observer(observer)