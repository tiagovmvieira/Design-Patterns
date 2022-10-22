from termcolor import colored
from enum import Enum

class SizeEnum(Enum):
    TALL = 'tall'
    GRANDE = 'grande'
    VENTI = 'venti'

class Beverage():
    def __init__(self, description: str, size: SizeEnum = SizeEnum.GRANDE)-> None:
        self.description = description
        self.size = size

    def get_description(self)-> str:
        return self.description

    def set_size(self, size: SizeEnum)-> None:
        self.size = size

    def get_size(self)-> SizeEnum:
        return self.size

    def cost(self)-> int:
        return 0 #if we want to apply a base price for each beverage, we should update this value

class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage)-> None:
        self.beverage = beverage

    @Beverage
    def beverage(self)-> Beverage:
        return self.beverage

    def set_size(self, size: SizeEnum)-> None:
        self.size = size

    def get_size(self)-> SizeEnum:
        return self.beverage.get_size()
    
    def get_description(self) -> str:
        return self.get_description()

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
        base_beverage_cost = self.beverage.cost()
        if self.beverage.get_size() == SizeEnum.VENTI:
            return base_beverage_cost + 0.7
        elif self.beverage.get_size() == SizeEnum.GRANDE:
            return base_beverage_cost + 0.10
        elif self.beverage.get_size() == SizeEnum.TALL:
            return base_beverage_cost + 0.13

class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage)-> None:
        super().__init__(beverage)

    def get_description(self)-> str:
        return self.beverage.get_description() + ", Mocha" if self.beverage.get_description() != "" else "Mocha"

    def cost(self)-> float:
        base_beverage_cost = self.beverage.cost()
        if self.beverage.get_size() == SizeEnum.VENTI:
            return base_beverage_cost + 0.13
        elif self.beverage.get_size() == SizeEnum.GRANDE:
            return base_beverage_cost + 0.20
        elif self.beverage.get_size() == SizeEnum.TALL:
            return base_beverage_cost + 0.27

class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage)-> None:
        super().__init__(beverage)

    def get_description(self)-> str:
        return self.beverage.get_description() + ", Soy" if self.beverage.get_description() != "" else "Soy"

    def cost(self)-> float:
        base_beverage_cost = self.beverage.cost()
        if self.beverage.get_size() == SizeEnum.VENTI:
            return base_beverage_cost + 0.10
        elif self.beverage.get_size() == SizeEnum.GRANDE:
            return base_beverage_cost + 0.15
        elif self.beverage.get_size() == SizeEnum.TALL:
            return base_beverage_cost + 0.20 

class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage)-> None:
        super().__init__(beverage)

    def get_description(self)-> str:
        return self.beverage.get_description() + ", Whip" if self.beverage.get_description() != "" else "Whip"

    def cost(self)-> float:
        base_beverage_cost = self.beverage.cost()
        if self.beverage.get_size() == SizeEnum.VENTI:
            return base_beverage_cost + 0.07
        elif self.beverage.get_size() == SizeEnum.GRANDE:
            return base_beverage_cost + 0.10
        elif self.beverage.get_size() == SizeEnum.TALL:
            return base_beverage_cost + 0.13

if __name__ == '__main__':
    print(colored('----------------- DECORATOR PATTERN -----------------', 'white'))
    print(colored('--------------------- EXPRESSO ----------------------', 'blue'))
    expresso = Expresso()
    print(expresso.get_description())
    print(f"{expresso.cost():.2f}", "€", '\n')

    print(colored('--------------------- DARK ROAST --------------------', 'red'))
    dark_roast = DarkRoast()
    dark_roast.set_size(SizeEnum.VENTI)
    dark_roast = Mocha(dark_roast)
    dark_roast = Whip(dark_roast)
    print(dark_roast.get_description())
    print(f"{dark_roast.cost():.2f}", "€",'\n')

    print(colored('-------------------- HOUSE BLEND --------------------', 'green'))
    house_blend = HouseBlend()
    house_blend.set_size(SizeEnum.TALL)
    house_blend = Soy(house_blend)
    house_blend = Mocha(house_blend)
    house_blend = SteamedMilk(house_blend)
    print(house_blend.get_description())
    print(f"{house_blend.cost():.2f}", '€','\n')

    print(colored('----------------------- DECAF -----------------------', 'yellow'))
    decaf = Decaf()
    decaf.set_size(SizeEnum.GRANDE)
    decaf = Soy(decaf)
    decaf = Mocha(decaf)
    decaf = SteamedMilk(decaf)
    decaf = Whip(decaf)
    print(decaf.get_description())
    print(f"{decaf.cost():.2f}", '€', '\n')

    print(colored('---------------- SIMPLE STEAMED MILK ----------------', 'grey'))
    steamed_milk = Beverage('')
    steamed_milk.set_size(SizeEnum.GRANDE)
    steamed_milk = SteamedMilk(steamed_milk)
    print(steamed_milk.get_description())
    print(f"{steamed_milk.cost():.2f}", '€','\n')
    
    print(colored('-------------------- SIMPLE MOCHA -------------------', 'grey'))
    mocha = Beverage('')
    mocha.set_size(SizeEnum.TALL)
    mocha = Mocha(mocha)
    print(mocha.get_description())
    print(mocha.cost(), '€','\n')

    print(colored('--------------------- SIMPLE SOY --------------------', 'grey'))
    soy = Beverage('')
    soy.set_size(SizeEnum.VENTI)
    soy = Soy(soy)
    print(soy.get_description())
    print(soy.cost(), '€','\n')

    print(colored('-------------------- SIMPLE WHIP --------------------', 'grey'))
    whip = Beverage('')
    print('Size', whip.get_size())
    whip = Whip(whip)
    print(whip.get_description())
    print(whip.cost(), '€')