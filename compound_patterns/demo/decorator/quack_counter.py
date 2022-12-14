from quackable import Quackable
from observer.observer import Observer

class QuackableComponent():
    def __init__(self, duck: Quackable):
        self.quackable = duck

    def quack(self)-> None:
        pass

class QuackCounter(QuackableComponent):
    _number_of_quacks: int = 0

    def __init__(self, duck: Quackable)-> None:
        self.quackable_component = duck

    @QuackableComponent
    def quackable_component(self)-> QuackableComponent:
        return self.quackable_component

    def quack(self)-> None:
        self.quackable_component.quack()
        QuackCounter._number_of_quacks += 1

    @staticmethod
    def reset_number_of_quacks()-> None:
        QuackCounter._number_of_quacks = 0

    @staticmethod
    def get_quacks()-> int:
        return QuackCounter._number_of_quacks

    def notify_observers(self)-> None:
        self.quackable_component.notify_observers()

    def register_observer(self, observer: Observer)-> None:
        self.quackable_component.register_observer(observer)