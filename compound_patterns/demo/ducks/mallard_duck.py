from quackable import Quackable
from observer.observer import Observer
from observer.observable import Observable

class MallardDuck(Quackable):
    def __init__(self)-> None:
        self.observable = Observable(self)

    def __str__(self)-> str:
        return "Mallard Duck"
    
    def notify_observers(self)-> None:
        self.observable.notify_observers()

    def quack(self)-> None:
        print("Quack")
        self.notify_observers()

    def register_observer(self, observer: Observer)-> None:
        self.observable.register_observer(observer)