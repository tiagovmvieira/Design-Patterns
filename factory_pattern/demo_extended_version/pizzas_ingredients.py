from __future__ import annotations

from abc import ABC, abstractmethod

class PizzaIngredient(ABC):
    def __init__(self, name: str)-> None:
        self.name = name

    def get_name(self)-> str:
        return self.name

class MarinaraSauce(PizzaIngredient):
    def __init__(self, name="Marina Sauce"):
        super().__init__(name)

class PlumTomatoSauce(PizzaIngredient):
    def __init__(self, name="Plum Tomato Sauce"):
        super().__init__(name)

class ReggianoCheese(PizzaIngredient):
    def __init__(self, name="Reggiano Cheese"):
        super().__init__(name)

class Mozzarella(PizzaIngredient):
    def __init__(self, name="Mozzarella"):
        super().__init__(name)

class Parmesan(PizzaIngredient):
    def __init__(self, name="Parmesan"):
        super().__init__(name)

class Oregano(PizzaIngredient):
    def __init__(self, name="Oregano"):
        super().__init__(name)

class Clams(PizzaIngredient):
    def __init__(self, name="Clams"):
        super().__init__(name)

class FreshClams(PizzaIngredient):
    def __init__(self, name="Fresh Clams"):
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

class SlicedPepperoni(PizzaIngredient):
    def __init__(self, name="Sliced Pepperoni"):
        super().__init__(name)

class Garlic(PizzaIngredient):
    def __init__(self, name="Garlic"):
        super().__init__(name)

class ThinCrustDough(PizzaIngredient):
    def __init__(self, name="Thin Crust Dough"):
        super().__init__(name)

class ThickCrustDough(PizzaIngredient):
    def __init__(self, name="Thick Crust Dough"):
        super().__init__(name)