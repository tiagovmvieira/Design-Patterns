from quackable import Quackable
from observer.observer import Observer

from typing import List
from collections.abc import Iterator, Iterable

class FlockIterator(Iterator):
    def __init__(self, quackables: List[Quackable])-> None:
        self.quackables = quackables
        self.position = 0

    def __next__(self)-> Quackable:
        try:
            quackable = self.quackables[self.position]
            self.position += 1
        except IndexError:
            raise StopIteration()
        
        return quackable

class Flock(Quackable, Iterable):
    def __init__(self)-> None:
        self.quackables: List[Quackable] = []

    def __iter__(self)-> FlockIterator:
        return FlockIterator(self.quackables)

    def __str__(self)-> str:
        return "Flock of Ducks"

    def add(self, quackable: Quackable)-> None:
        self.quackables.append(quackable)

    def quack(self)-> None:
        for quackable in self.quackables:
            quackable.quack()

    def notify_observers(self)-> None:
        pass

    def register_observer(self, observer: Observer)-> None:
        for quackable in self.quackables:
            quackable.register_observer(observer)