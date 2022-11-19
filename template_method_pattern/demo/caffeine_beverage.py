from abc import ABC, abstractmethod
from typing import final

class CaffeineBeverage(ABC):
    def __init__(self):
        if self.__class__ == CaffeineBeverage:
            raise TypeError("Instantiating the Abstract Class")

    # this final decorator indicates to type checkers that the decorated method cannot be overriden
    @final 
    def prepare_recipe(self)-> None:
        self._boil_water()
        self._brew()
        self._pour_in_cup()
        self._add_condiments()

    @abstractmethod
    def _brew(self):
        pass

    @abstractmethod
    def _add_condiments(self):
        pass

    @final
    def _boil_water(self):
        print("Boiling water")

    @final
    def _pour_in_cup(self):
        print("Pouring into cup")