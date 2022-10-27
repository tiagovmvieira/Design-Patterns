from termcolor import colored

class PizzaStore():
    def __init__(self, pizza_factory_name: str)-> None:
        self.pizza_factory = SimplePizzaFactory(pizza_factory_name)

    def order_pizza(self, pizza_name: str):
        return self.pizza_factory.make_pizza(pizza_name)

class SimplePizzaFactory():
    def __init__(self, pizza_factory_name: str)-> None:
        self.pizza_factory_name = pizza_factory_name

    def make_pizza(self, pizza_name: str):
        if pizza_name == "CheesePizza":
            return CheesePizza()
        elif pizza_name == "PepperoniPizza":
            return PepperoniPizza()
        elif pizza_name == "ClamPizza":
            return ClamPizza()
        elif pizza_name == "VeggiePizza":
            return VeggiePizza()

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

class CheesePizza(Pizza):
    def __init__(self, name="CheesePizza"):
        super().__init__(name)

class VeggiePizza(Pizza):
    def __init__(self, name="VeggiePizza"):
        super().__init__(name)

class ClamPizza(Pizza):
    def __init__(self, name="ClamPizza"):
        super().__init__(name)

class PepperoniPizza(Pizza):
    def __init__(self, name="PepperoniPizza"):
        super().__init__(name)
    
if __name__ == '__main__':
    print(colored('------------------ SIMPLE FACTORY -----------------', 'white'))
    print(colored('----------------- ROME PIZZA STORE ----------------', 'white'))
    rome_pizza_store = PizzaStore("Milan Pizza Factory")

    print(colored('------------------- CHEESE PIZZA ------------------', 'blue'))
    cheese_pizza = rome_pizza_store.order_pizza("CheesePizza")
    print(cheese_pizza.prepare())
    print(cheese_pizza.bake())
    print(cheese_pizza.cut())
    print(cheese_pizza.box(),'\n')

    print(colored('------------------- VEGGIE PIZZA ------------------', 'yellow'))
    veggie_pizza = rome_pizza_store.order_pizza("VeggiePizza")
    print(veggie_pizza.prepare())
    print(veggie_pizza.bake())
    print(veggie_pizza.cut())
    print(veggie_pizza.box(),'\n')
    
    print(colored('-------------------- CLAM PIZZA -------------------', 'green'))
    clam_pizza = rome_pizza_store.order_pizza("ClamPizza")
    print(clam_pizza.prepare())
    print(clam_pizza.bake())
    print(clam_pizza.cut())
    print(clam_pizza.box(),'\n')

    print(colored('----------------- PEPPERONI PIZZA -----------------', 'red'))
    pepperoni_pizza = rome_pizza_store.order_pizza("PepperoniPizza")
    print(pepperoni_pizza.prepare())
    print(pepperoni_pizza.bake())
    print(pepperoni_pizza.cut())
    print(pepperoni_pizza.box())