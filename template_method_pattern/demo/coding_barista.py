from coffee import Coffee
from tea import Tea

from termcolor import colored

if __name__ == '__main__':
    print(colored('------------- TEMPLATE METHOD PATTERN -------------', 'white'))
    print(colored('------------------- TEA REQUEST -------------------', 'blue'))
    tea = Tea()
    tea.prepare_recipe()

    print(colored('\n------------------ COFFEE REQUEST -----------------', 'green'))
    coffee = Coffee()
    coffee.prepare_recipe()