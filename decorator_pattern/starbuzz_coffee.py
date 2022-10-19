from termcolor import colored

class Beverage():
    def __init__(self, description: str):
        self.description = description

    def get_description(self)-> str:
        return self.description

    def cost(self)-> int:
        return 0 #if we want to apply a base price for each beverage, we should update this value

class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage)-> None:
        self.beverage = beverage

    @Beverage
    def beverage(self)-> Beverage:
        return self.beverage
    
    def get_description(self) -> str:
        return self.get_description()
        
    def cost(self)-> float:
        return self.beverage.cost()

class HouseBlend(Beverage):
    def __init__(self, description: str = "House Blend Coffee")-> None:
        super().__init__(description)

    def cost(self)-> float:
        return 0.89

class DarkRoast(Beverage):
    def __init__(self, description: str = "Dark Roast Coffee")-> None:
        super().__init__(description)

    def cost(self)-> float:
        return 0.99

class Expresso(Beverage):
    def __init__(self, description : str = "Expresso")-> None:
        super().__init__(description)

    def cost(self)-> float:
        return 1.99

class Decaf(Beverage):
    def __init__(self, description: str = "Decaf Coffee")-> None:
        super().__init__(description)

    def cost(self)-> float:
        return 1.05

class SteamedMilk(CondimentDecorator):
    def __init__(self, beverage: Beverage)-> None:
        super().__init__(beverage)

    def get_description(self)-> str:
        return self.beverage.get_description() + ", Steamed Milk" if self.beverage.get_description() != "" else "Steamed Milk"

    def cost(self)-> float:
        return self.beverage.cost() + 0.10

class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage)-> None:
        super().__init__(beverage)

    def get_description(self)-> str:
        return self.beverage.get_description() + ", Mocha" if self.beverage.get_description() != "" else "Mocha"

    def cost(self)-> float:
        return self.beverage.cost() + 0.20

class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage)-> None:
        super().__init__(beverage)

    def get_description(self)-> str:
        return self.beverage.get_description() + ", Soy" if self.beverage.get_description() != "" else "Soy"

    def cost(self)-> float:
        return self.beverage.cost() + 0.15

class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage)-> None:
        super().__init__(beverage)

    def get_description(self)-> str:
        return self.beverage.get_description() + ", Whip" if self.beverage.get_description() != "" else "Whip"

    def cost(self)-> float:
        return self.beverage.cost() + 0.10 

if __name__ == '__main__':
    print(colored('----------------- DECORATOR PATTERN -----------------', 'white'))
    print(colored('--------------------- EXPRESSO ----------------------', 'blue'))
    expresso = Expresso()
    print(expresso.get_description())
    print(expresso.cost(), "€", '\n')

    print(colored('--------------------- DARK ROAST --------------------', 'red'))
    dark_roast = DarkRoast()
    dark_roast = Mocha(dark_roast)
    dark_roast = Mocha(dark_roast)
    dark_roast = Whip(dark_roast)
    print(dark_roast.get_description())
    print(dark_roast.cost(), "€",'\n')

    print(colored('-------------------- HOUSE BLEND --------------------', 'green'))
    house_blend = HouseBlend()
    house_blend = Soy(house_blend)
    house_blend = Mocha(house_blend)
    house_blend = SteamedMilk(house_blend)
    print(house_blend.get_description())
    print(house_blend.cost(), '€','\n')

    print(colored('---------------- SIMPLE STEAMED MILK ----------------', 'yellow'))
    steamed_milk = Beverage('')
    steamed_milk = SteamedMilk(steamed_milk)
    print(steamed_milk.get_description())
    print(steamed_milk.cost(), '€','\n')
    
    print(colored('-------------------- SIMPLE MOCHA -------------------', 'yellow'))
    mocha = Beverage('')
    mocha = Mocha(mocha)
    print(mocha.get_description())
    print(mocha.cost(), '€','\n')

    print(colored('--------------------- SIMPLE SOY --------------------', 'yellow'))
    soy = Beverage('')
    soy = Soy(soy)
    print(soy.get_description())
    print(soy.cost(), '€','\n')

    print(colored('-------------------- SIMPLE WHIP --------------------', 'yellow'))
    whip = Beverage('')
    whip = Whip(whip)
    print(whip.get_description())
    print(whip.cost(), '€')