from __future__ import annotations

from pizza_factory_pattern_extended import *

from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self, name: str)-> None:
        if self.__class__ == PizzaStore:
            raise TypeError("Instantiating the Abstract Class")

        self.name = name
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.pepperoni = None
        self.clams = None
        self.veggies = []

    def set_name(self, name: str)-> None:
        self.name = name

    def get_name(self)-> str:
        return self.name
    
    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        return "Bake for 25 minutes at 350 C"

    def cut(self):
        return "Cutting the pizza into diagonal slices"

    def box(self):
        return "Place pizza in official PizzaStore box"

class  NYStyleCheesePizza(Pizza):
    def __init__(self, name="NYStyleCheesePizza", ingredient_factory = NYPizzaIngredientFactory()):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheeses()
        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese(s) -> {self.cheese.get_name()}"
        
class NYStylePepperoniPizza(Pizza):
    def __init__(self, name="NYStylePepperoniPizza", ingredient_factory = NYPizzaIngredientFactory()):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheeses()
        self.pepperoni = self.ingredient_factory.create_pepperoni()
        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese(s) -> {self.cheese.get_name()}, Pepperoni -> {self.pepperoni.get_name()}"

class NYStyleClamPizza(Pizza):
    def __init__(self, name="NYStyleClamPizza", ingredient_factory = NYPizzaIngredientFactory()):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheeses()
        self.clams = self.ingredient_factory.create_clam()
        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese(s) -> {self.cheese.get_name()}, Clam -> {self.clams.get_name()}"

class NYStyleVeggiePizza(Pizza):
    def __init__(self, name="NYStyleVeggiePizza", ingredient_factory = NYPizzaIngredientFactory()):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheeses()
        self.veggies = self.ingredient_factory.create_veggies()
        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese(s) -> {self.cheese.get_name()}"

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self, name="ChicagoStyleCheesePizza", ingredient_factory = ChicagoPizzaIngredientFactory()):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self, name="ChicagoStylePepperoniPizza"):
        super().__init__(name)

class ChicagoStyleClamPizza(Pizza):
    def __init__(self, name="ChicagoStyleClamPizza"):
        super().__init__(name)

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self, name="ChicagoStyleVeggiePizza"):
        super().__init__(name)