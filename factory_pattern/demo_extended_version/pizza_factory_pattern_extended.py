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
            return NYStyleCheesePizza(ingredient_factory = NYPizzaIngredientFactory())
        elif pizza_name == "PepperoniPizza":
            return NYStylePepperoniPizza(ingredient_factory = NYPizzaIngredientFactory())
        elif pizza_name == "ClamPizza":
            return NYStyleClamPizza(ingredient_factory = NYPizzaIngredientFactory())
        elif pizza_name == "VeggiePizza":
            return NYStyleVeggiePizza(ingredient_factory = NYPizzaIngredientFactory())

class ChicagoStylePizzaStore(PizzaStore):
    def __init__(self):
        super().__init__()

    def create_pizza(self, pizza_name: str)-> Pizza:
        if pizza_name == "CheesePizza":
            return ChicagoStyleCheesePizza(ingredient_factory = ChicagoPizzaIngredientFactory())
        elif pizza_name == "PepperoniPizza":
            return ChicagoStylePepperoniPizza(ingredient_factory = ChicagoPizzaIngredientFactory())
        elif pizza_name == "ClamPizza":
            return ChicagoStyleClamPizza(ingredient_factory = ChicagoPizzaIngredientFactory())
        elif pizza_name == "VeggiePizza":
            return ChicagoStyleVeggiePizza(ingredient_factory = ChicagoPizzaIngredientFactory())

class CaliforniaStylePizzaStore(PizzaStore):
    def __init__(self):
        super().__init__()

    def create_pizza(self, pizza_name: str)-> Pizza:
        if pizza_name == "CheesePizza":
            return CaliforniaStyleCheesePizza(ingredient_factory = CaliforniaPizzaIngredientFactory())
        elif pizza_name == "PepperoniPizza":
            return CaliforniaStylePepperoniPizza(ingredient_factory = CaliforniaPizzaIngredientFactory())
        elif pizza_name == "ClamPizza":
            return CaliforniaStyleClamPizza(ingredient_factory = CaliforniaPizzaIngredientFactory())
        elif pizza_name == "VeggiePizza":
            return CaliforniaStyleVeggiePizza(ingredient_factory = CaliforniaPizzaIngredientFactory())

class PizzaIngredientsFactory(ABC):
    @abstractmethod
    def create_dough():
        pass

    @abstractmethod
    def create_sauce():
        pass

    @abstractmethod
    def create_cheese():
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

    def create_cheese(self):
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

    def create_cheese(self)-> List:
        cheeses = [Mozzarella(), Parmesan()]
        return cheeses

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_veggies(self)-> List[PizzaIngredient]:
        veggies = [Oregano(), Eggplant(), Spinach(), BlackOlives()]
        return veggies

    def create_clam(self):
        return FrozenClams()

class CaliforniaPizzaIngredientFactory(PizzaIngredientsFactory):
    def __init__(self):
        pass

    def create_dough(self):
        return VeryThinCrustDough()

    def create_sauce(self):
        return BruschettaSauce()

    def create_cheese(self):
        return GoatCheese()

    def create_pepperoni(self):
        return SlicedPepperoni()
        
    def create_veggies(self)-> List[PizzaIngredient]:
        veggies = [Tomato(), Eggplant(), Mushrooms(), BlackOlives()]
        return veggies

    def create_clam(self):
        return FreshClams()

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

    print(colored('-------------- CHICAGO PIZZA STORE ----------------', 'white'))
    ch_pizza_store = ChicagoStylePizzaStore()

    print(colored('------------------- CHEESE PIZZA ------------------', 'blue'))
    ch_cheese_pizza = ch_pizza_store.order_pizza("CheesePizza")
    print(ch_cheese_pizza.prepare())
    print(ch_cheese_pizza.bake())
    print(ch_cheese_pizza.cut())
    print(ch_cheese_pizza.box(),'\n')

    print(colored('------------------- VEGGIE PIZZA ------------------', 'yellow'))
    ch_veggie_pizza = ch_pizza_store.order_pizza("VeggiePizza")
    print(ch_veggie_pizza.prepare())
    print(ch_veggie_pizza.bake())
    print(ch_veggie_pizza.cut())
    print(ch_veggie_pizza.box(),'\n')

    print(colored('-------------------- CLAM PIZZA -------------------', 'green'))
    ch_clam_pizza = ch_pizza_store.order_pizza("ClamPizza")
    print(ch_clam_pizza.prepare())
    print(ch_clam_pizza.bake())
    print(ch_clam_pizza.cut())
    print(ch_clam_pizza.box(),'\n')

    print(colored('----------------- PEPPERONI PIZZA -----------------', 'red'))
    ch_pepperoni_pizza = ch_pizza_store.order_pizza("PepperoniPizza")
    print(ch_pepperoni_pizza.prepare())
    print(ch_pepperoni_pizza.bake())
    print(ch_pepperoni_pizza.cut())
    print(ch_pepperoni_pizza.box(),'\n')

    print(colored('------------- CALIFORNIA PIZZA STORE --------------', 'white'))
    ca_pizza_store = CaliforniaStylePizzaStore()

    print(colored('------------------- CHEESE PIZZA ------------------', 'blue'))
    ca_cheese_pizza = ca_pizza_store.order_pizza("CheesePizza")
    print(ca_cheese_pizza.prepare())
    print(ca_cheese_pizza.bake())
    print(ca_cheese_pizza.cut())
    print(ca_cheese_pizza.box(),'\n')

    print(colored('------------------- VEGGIE PIZZA ------------------', 'yellow'))
    ca_veggie_pizza = ca_pizza_store.order_pizza("VeggiePizza")
    print(ca_veggie_pizza.prepare())
    print(ca_veggie_pizza.bake())
    print(ca_veggie_pizza.cut())
    print(ca_veggie_pizza.box(),'\n')

    print(colored('-------------------- CLAM PIZZA -------------------', 'green'))
    ca_clam_pizza = ca_pizza_store.order_pizza("ClamPizza")
    print(ca_clam_pizza.prepare())
    print(ca_clam_pizza.bake())
    print(ca_clam_pizza.cut())
    print(ca_clam_pizza.box(),'\n')

    print(colored('----------------- PEPPERONI PIZZA -----------------', 'red'))
    ca_pepperoni_pizza = ca_pizza_store.order_pizza("PepperoniPizza")
    print(ca_pepperoni_pizza.prepare())
    print(ca_pepperoni_pizza.bake())
    print(ca_pepperoni_pizza.cut())
    print(ca_pepperoni_pizza.box(),'\n')