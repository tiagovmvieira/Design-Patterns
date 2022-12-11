from observer.quack_observable import QuackObservable
from observer.observer import Observer

from typing import List

class Observable(QuackObservable):
    def __init__(self, duck: QuackObservable)-> None:
        self.observers: List[Observer] = []
        self.duck = duck

    def register_observer(self, observer: Observer)-> None:
        self.observers.append(observer)

    def notify_observers(self)-> None:
        for observer in self.observers:
            observer.update(self.duck)