from termcolor import colored

class Beverage():
    def __init__(self, description: str):
        self.description = description

    def get_description(self)-> str:
        return self.description

    def cost():
        pass

class HouseBlend(Beverage):
    def __init__(self, description: str):
        super().__init__(description)

class DarkRoast(Beverage):
    def __init__(self, description: str):
        super().__init__(description)

class Expresso(Beverage):
    def __init__(self, description: str):
        super().__init__(description)

class Decaf(Beverage):
    def __init__(self, description: str):
        super().__init__(description)

class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage)-> None:
        self.beverage = beverage

class Milk(CondimentDecorator):
    def cost():
        pass

    def get_description():
        pass

class Mocha(CondimentDecorator):
    def cost():
        pass

    def get_description():
        pass

class Soy(CondimentDecorator):
    def cost():
        pass

    def get_description():
        pass

class Whip(CondimentDecorator):
    def cost():
        pass

    def get_description():
        pass

if __name__ == '__main__':
    print(colored('----------------- DECORATOR PATTERN -----------------', 'white'))
