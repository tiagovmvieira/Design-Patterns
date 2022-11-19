from coffee import Coffee, CoffeeWithHook
from tea import Tea, TeaWithHook

from termcolor import colored

if __name__ == '__main__':
    print(colored('------------- TEMPLATE METHOD PATTERN -------------', 'white'))
    print(colored('----------------- SIMPLE REQUEST ------------------', 'white'))
    print(colored('------------------- TEA REQUEST -------------------', 'blue'))
    tea = Tea()
    tea.prepare_recipe()

    print(colored('\n------------------ COFFEE REQUEST -----------------', 'green'))
    coffee = Coffee()
    coffee.prepare_recipe()

    print(colored('\n---------- CONDIMENTS SPECIFIED REQUEST -----------', 'white'))
    print(colored('------------------- TEA REQUEST -------------------', 'blue'))
    tea_with_hook = TeaWithHook()
    tea_with_hook.prepare_recipe()

    print(colored('\n------------------ COFFEE REQUEST -----------------', 'green'))
    coffee_with_hook = CoffeeWithHook()
    coffee_with_hook.prepare_recipe()
