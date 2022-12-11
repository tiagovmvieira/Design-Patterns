from quackable import Quackable
from ducks.goose_duck import GooseDuck
from observer.observable import Observable
from observer.observer import Observer

class GooseDuckAdapter(Quackable):
    def __init__(self, goose: GooseDuck)-> None:
        self.goose = goose
        self.observable = Observable(self)

    def __str__(self)-> str:
        return "Goose pretending to be a Duck"

    def notify_observers(self)-> None:
        self.observable.notify_observers()

    def quack(self)-> None:
        self.goose.honk()
        self.notify_observers()

    def register_observer(self, observer: Observer)-> None:
        self.observable.register_observer(observer)
