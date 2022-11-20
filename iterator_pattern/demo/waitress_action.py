from waitress import Waitress
from termcolor import colored

if __name__ == '__main__':
    print(colored('------------------ ITERATOR PATTERN -----------------', 'white'))
    waitress = Waitress()
    waitress.print_menu()