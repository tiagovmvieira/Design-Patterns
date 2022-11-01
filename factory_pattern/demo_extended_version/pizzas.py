from __future__ import annotations

from pizza_factory_pattern_extended import *

from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self, name: str)-> None:
        if self.__class__ == Pizza:
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

class NYStyleCheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientsFactory, name="NYStyleCheesePizza", ):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()[0]
        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese -> {self.cheese.get_name()}, Veggies -> {self.veggies.get_name()}"
        
class NYStylePepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientsFactory, name="NYStylePepperoniPizza"):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()[1:]
        self.pepperoni = self.ingredient_factory.create_pepperoni()

        usable_veggies = ""
        for veggie in self.veggies:
            usable_veggies += veggie.get_name() + " "
        usable_veggies = usable_veggies[:-1]
        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese -> {self.cheese.get_name()}, Veggies -> {usable_veggies}, Pepperoni -> {self.pepperoni.get_name()}"

class NYStyleClamPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientsFactory, name="NYStyleClamPizza"):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clams = self.ingredient_factory.create_clam()
        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese -> {self.cheese.get_name()}, Clam -> {self.clams.get_name()}"

class NYStyleVeggiePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientsFactory, name="NYStyleVeggiePizza"):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()[1:]

        usable_veggies = ""
        for veggie in self.veggies:
            usable_veggies += veggie.get_name() + " "
        usable_veggies = usable_veggies[:-1]

        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese -> {self.cheese.get_name()}, Veggies -> {usable_veggies}"

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientsFactory, name="ChicagoStyleCheesePizza"):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()[0]

        usable_cheeses = ""
        for cheese in self.cheese:
            usable_cheeses += cheese.get_name() + " "
        usable_cheeses = usable_cheeses[:-1]

        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese -> {usable_cheeses}, Veggies -> {self.veggies.get_name()}"

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientsFactory, name="ChicagoStylePepperoniPizza"):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()
        self.pepperoni = self.ingredient_factory.create_pepperoni()

        usable_cheeses = ""
        for cheese in self.cheese:
            usable_cheeses += cheese.get_name() + " "
        usable_cheeses = usable_cheeses[:-1]

        usable_veggies = ""
        for veggie in self.veggies:
            usable_veggies += veggie.get_name() + " "
        usable_veggies = usable_veggies[:-1]

        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese -> {usable_cheeses}, Veggies -> {usable_veggies}, Pepperoni -> {self.pepperoni.get_name()}"

class ChicagoStyleClamPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientsFactory, name="ChicagoStyleClamPizza"):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()
        self.clams = self.ingredient_factory.create_clam()

        usable_cheeses = ""
        for cheese in self.cheese:
            usable_cheeses += cheese.get_name() + " "
        usable_cheeses = usable_cheeses[:-1]

        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese -> {usable_cheeses}, Clam -> {self.clams.get_name()}"

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientsFactory, name="ChicagoStyleVeggiePizza"):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()[1:]

        usable_cheeses = ""
        for cheese in self.cheese:
            usable_cheeses += cheese.get_name() + " "
        usable_cheeses = usable_cheeses[:-1]

        usable_veggies = ""
        for veggie in self.veggies:
            usable_veggies += veggie.get_name() + " "
        usable_veggies = usable_veggies[:-1]

        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese -> {usable_cheeses}, Veggies -> {usable_veggies}"

class CaliforniaStyleCheesePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientsFactory, name="CaliforniaStyleCheesePizza"):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()[0]

        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese -> {self.cheese.get_name()}, Veggies -> {self.veggies.get_name()}"

class CaliforniaStylePepperoniPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientsFactory, name="CaliforniaStylePepperoniPizza"):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.pepperoni = self.ingredient_factory.create_pepperoni()
        self.veggies = self.ingredient_factory.create_veggies()

        usable_veggies = ""
        for veggie in self.veggies:
            usable_veggies += veggie.get_name() + " "
        usable_veggies = usable_veggies[:-1] 

        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese -> {self.cheese.get_name()}, Veggies -> {usable_veggies}, Pepperoni -> {self.pepperoni.get_name()}"

class CaliforniaStyleClamPizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientsFactory, name="CaliforniaStyleClamPizza"):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clams = self.ingredient_factory.create_clam()

        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese -> {self.cheese.get_name()}, Clams -> {self.clams.get_name()}s"

class CaliforniaStyleVeggiePizza(Pizza):
    def __init__(self, ingredient_factory: PizzaIngredientsFactory, name="CaliforniaStyleVeggiePizza"):
        super().__init__(name)
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()

        usable_veggies = ""
        for veggie in self.veggies:
            usable_veggies += veggie.get_name() + " "
        usable_veggies = usable_veggies[:-1]

        return f"Preparing {self.name}... Dough -> {self.dough.get_name()}, Sauce -> {self.sauce.get_name()}, Cheese -> {self.cheese.get_name()}, Veggies -> {usable_veggies}"