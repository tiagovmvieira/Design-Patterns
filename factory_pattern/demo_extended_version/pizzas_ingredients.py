from __future__ import annotations

from abc import ABC

class Dough(ABC):
    def __init__(self, name: str)-> None:
        if self.__class__ == Dough:
            raise TypeError("Instantiating the Abstract Class")
        self.name = name

    def get_name(self)-> str:
        return self.name

class ThinCrustDough(Dough):
    def __init__(self, name="Thin Crust Dough"):
        super().__init__(name)

class ThickCrustDough(Dough):
    def __init__(self, name="Thick Crust Dough"):
        super().__init__(name)

class VeryThinCrustDough(Dough):
    def __init__(self, name="Very Thin Crust Dough"):
        super().__init__(name)

class Sauce(ABC):
    def __init__(self, name: str)-> None:
        if self.__class__ == Sauce:
            raise TypeError("Instantiating the Abstract Class")
        self.name = name
    
    def get_name(self)-> str:
        return self.name

class MarinaraSauce(Sauce):
    def __init__(self, name="Marinara Sauce"):
        super().__init__(name)

class PlumTomatoSauce(Sauce):
    def __init__(self, name="Plum Tomato Sauce"):
        super().__init__(name)

class BruschettaSauce(Sauce):
    def __init__(self, name="Bruschetta Sauce"):
        super().__init__(name)

class Cheese(ABC):
    def __init__(self, name: str)-> None:
        if self.__class__ == Cheese:
            raise TypeError("Instantiating the Abstract Class")
        self.name = name

    def get_name(self)-> str:
        return self.name

class ReggianoCheese(Cheese):
    def __init__(self, name="Reggiano Cheese"):
        super().__init__(name)

class Mozzarella(Cheese):
    def __init__(self, name="Mozzarella Cheese"):
        super().__init__(name)

class Parmesan(Cheese):
    def __init__(self, name="Parmesan Cheese"):
        super().__init__(name)

class GoatCheese(Cheese):
    def __init__(self, name="Goat Cheese"):
        super().__init__(name)

class Clams(ABC):
    def __init__(self, name: str)-> None:
        if self.__class__ == Clams:
            raise TypeError("Instantiating the Abstract Class")
        self.name = name

    def get_name(self)-> str:
        return self.name

class FrozenClams(Clams):
    def __init__(self, name="Frozen Clams"):
        super().__init__(name)

class FreshClams(Clams):
    def __init__(self, name="Fresh Clams"):
        super().__init__(name)

class PizzaIngredient(ABC):
    def __init__(self, name: str)-> None:
        self.name = name

    def get_name(self)-> str:
        return self.name

class SlicedPepperoni(PizzaIngredient):
    def __init__(self, name="Sliced Pepperoni"):
        super().__init__(name)

class Oregano(PizzaIngredient):
    def __init__(self, name="Oregano"):
        super().__init__(name)

class Eggplant(PizzaIngredient):
    def __init__(self, name="Eggplant"):
        super().__init__(name)

class Spinach(PizzaIngredient):
    def __init__(self, name="Spinach"):
        super().__init__(name)

class Onions(PizzaIngredient):
    def __init__(self, name="Onions"):
        super().__init__(name)

class RedPeppers(PizzaIngredient):
    def __init__(self, name="Red Peppers"):
        super().__init__(name)

class Mushrooms(PizzaIngredient):
    def __init__(self, name="Mushrooms"):
        super().__init__(name)

class BlackOlives(PizzaIngredient):
    def __init__(self, name="Black Olives"):
        super().__init__(name)

class Garlic(PizzaIngredient):
    def __init__(self, name="Garlic"):
        super().__init__(name)

class Tomato(PizzaIngredient):
    def __init__(self, name="Tomato"):
        super().__init__(name)

