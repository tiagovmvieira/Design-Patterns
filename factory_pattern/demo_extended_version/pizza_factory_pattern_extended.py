from __future__ import annotations

from pizzas_ingredients import *
from pizzas import *

from abc import ABC, abstractmethod
from typing import List
from termcolor import colored

class PizzaStore(ABC):
    def __init__(self):
        if self.__class__ == PizzaStore:
            raise TypeError("Instantiating the Abstract Class")

    def order_pizza(self, pizza_name: str)-> Pizza:
        pizza = self.create_pizza(pizza_name)
        return pizza

    @abstractmethod
    def create_pizza(self):
        pass

class NYStylePizzaStore(PizzaStore):
    def __init__(self):
        super().__init__()

    def create_pizza(self, pizza_name: str)-> Pizza:
        if pizza_name == "CheesePizza":
            return NYStyleCheesePizza()
        elif pizza_name == "PepperoniPizza":
            return NYStylePepperoniPizza()
        elif pizza_name == "ClamPizza":
            return NYStyleClamPizza()
        elif pizza_name == "VeggiePizza":
            return NYStyleVeggiePizza()

class ChicagoStylePizzaStore(PizzaStore):
    def __init__(self):
        super().__init__()

    def create_pizza(self, pizza_name: str)-> Pizza:
        if pizza_name == "CheesePizza":
            return ChicagoStyleCheesePizza()
        elif pizza_name == "PepperoniPizza":
            return ChicagoStylePepperoniPizza()
        elif pizza_name == "ClamPizza":
            return ChicagoStyleClamPizza()
        elif pizza_name == "VeggiePizza":
            return ChicagoStyleVeggiePizza()

class PizzaIngredientsFactory(ABC):
    @abstractmethod
    def create_dough():
        pass

    @abstractmethod
    def create_sauce():
        pass

    @abstractmethod
    def create_cheeses():
        pass

    @abstractmethod
    def create_veggies():
        pass

    @abstractmethod
    def create_pepperoni():
        pass

    @abstractmethod
    def create_clam():
        pass

class NYPizzaIngredientFactory(PizzaIngredientsFactory):
    def __init__(self):
        pass

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheeses(self):
        return ReggianoCheese()

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_veggies(self)-> List[PizzaIngredient]:
        veggies = [Garlic(), Onions(), Mushrooms(), RedPeppers()]
        return veggies

    def create_clam(self):
        return FreshClams()

class ChicagoPizzaIngredientFactory(PizzaIngredientsFactory):
    def __init__(self):
        pass

    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheeses(self)-> List:
        cheeses = [Mozzarella(), Parmesan()]
        return cheeses

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_veggies()-> List[PizzaIngredient]:
        veggies = [Oregano(), Eggplant(), Spinach(), BlackOlives()]
        return veggies

    def create_clam(self):
        return Clams()

if __name__ == '__main__':
    print(colored('----------------- FACTORY PATTERN -----------------', 'white'))
    print(colored('-------------- NEW YORK PIZZA STORE ---------------', 'white'))
    ny_pizza_store = NYStylePizzaStore()

    print(colored('------------------- CHEESE PIZZA ------------------', 'blue'))
    ny_cheese_pizza = ny_pizza_store.order_pizza("CheesePizza")
    print(ny_cheese_pizza.prepare())
    print(ny_cheese_pizza.bake())
    print(ny_cheese_pizza.cut())
    print(ny_cheese_pizza.box(),'\n')

    print(colored('------------------- VEGGIE PIZZA ------------------', 'yellow'))
    ny_veggie_pizza = ny_pizza_store.order_pizza("VeggiePizza")
    print(ny_veggie_pizza.prepare())
    print(ny_veggie_pizza.bake())
    print(ny_veggie_pizza.cut())
    print(ny_veggie_pizza.box(),'\n')
    
    print(colored('-------------------- CLAM PIZZA -------------------', 'green'))
    ny_clam_pizza = ny_pizza_store.order_pizza("ClamPizza")
    print(ny_clam_pizza.prepare())
    print(ny_clam_pizza.bake())
    print(ny_clam_pizza.cut())
    print(ny_clam_pizza.box(),'\n')

    print(colored('----------------- PEPPERONI PIZZA -----------------', 'red'))
    ny_pepperoni_pizza = ny_pizza_store.order_pizza("PepperoniPizza")
    print(ny_pepperoni_pizza.prepare())
    print(ny_pepperoni_pizza.bake())
    print(ny_pepperoni_pizza.cut())
    print(ny_pepperoni_pizza.box(),'\n')
