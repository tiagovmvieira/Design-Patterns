from __future__ import annotations
from termcolor import colored
from abc import abstractmethod

class PizzaStore():
    def __init__(self)-> None:
        pass

    def order_pizza(self, pizza_name: str)-> Pizza:
        pizza = self.create_pizza(pizza_name)
        return pizza

    @abstractmethod
    def create_pizza(self):
        pass

class NYStylePizzaStore(PizzaStore):
    def __init__(self):
        super().__init__()

    def create_pizza(self, pizza_name: str):
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

    def create_pizza(self, pizza_name: str):
        if pizza_name == "CheesePizza":
            return ChicagoStyleCheesePizza()
        elif pizza_name == "PepperoniPizza":
            return ChicagoStylePepperoniPizza()
        elif pizza_name == "ClamPizza":
            return ChicagoStyleClamPizza()
        elif pizza_name == "VeggiePizza":
            return ChicagoStyleVeggiePizza()

class Pizza():
    def __init__(self, name: str)-> None:
        self.name = name

    def prepare(self):
        return f"I am preparing a {self.name}!"

    def bake(self):
        return f"I am baking a {self.name}!"

    def cut(self):
        return f"I am cutting a {self.name}!"

    def box(self):
        return f"I am boxing a {self.name}!"

class NYStyleCheesePizza(Pizza):
    def __init__(self, name="NYStyleCheesePizza"):
        super().__init__(name)

class NYStylePepperoniPizza(Pizza):
    def __init__(self, name="NYStylePepperoniPizza"):
        super().__init__(name)

class NYStyleClamPizza(Pizza):
    def __init__(self, name="NYStyleClamPizza"):
        super().__init__(name)

class NYStyleVeggiePizza(Pizza):
    def __init__(self, name="NYStyleVeggiePizza"):
        super().__init__(name)

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self, name="ChicagoStyleCheesePizza"):
        super().__init__(name)

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self, name="ChicagoStylePepperoniPizza"):
        super().__init__(name)

class ChicagoStyleClamPizza(Pizza):
    def __init__(self, name="ChicagoStyleClamPizza"):
        super().__init__(name)

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self, name="ChicagoStyleVeggiePizza"):
        super().__init__(name)

if __name__ == '__main__':
    print(colored('----------------- FACTORY PATTERN -----------------', 'white'))
    print(colored('-------------- NEW YORK PIZZA STORE ---------------', 'white'))
    ny_pizza_store = NYStylePizzaStore()

    print(colored('------------------- CHEESE PIZZA ------------------', 'blue'))
    ny_cheese_pizza = ny_pizza_store.order_pizza("CheesePizza")
    print(ny_cheese_pizza.box(),'\n')

    print(colored('------------------- VEGGIE PIZZA ------------------', 'yellow'))
    ny_veggie_pizza = ny_pizza_store.order_pizza("VeggiePizza")
    print(ny_veggie_pizza.box(),'\n')

    print(colored('-------------------- CLAM PIZZA -------------------', 'green'))
    ny_clam_pizza = ny_pizza_store.order_pizza("ClamPizza")
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
    print(ch_cheese_pizza.box(),'\n')

    print(colored('------------------- VEGGIE PIZZA ------------------', 'yellow'))
    ch_veggie_pizza = ch_pizza_store.order_pizza("VeggiePizza")
    print(ch_veggie_pizza.box(),'\n')

    print(colored('-------------------- CLAM PIZZA -------------------', 'green'))
    ch_clam_pizza = ch_pizza_store.order_pizza("ClamPizza")
    print(ch_clam_pizza.box(),'\n')

    print(colored('----------------- PEPPERONI PIZZA -----------------', 'red'))
    ch_pepperoni_pizza = ch_pizza_store.order_pizza("PepperoniPizza")
    print(ch_pepperoni_pizza.prepare())
    print(ch_pepperoni_pizza.bake())
    print(ch_pepperoni_pizza.cut())
    print(ch_pepperoni_pizza.box(),'\n')

