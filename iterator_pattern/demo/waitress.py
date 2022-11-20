from diner_menu import DinerMenu
from pancake_house_menu import PancakeHouseMenu

class Waitress:
    def __init__(self, pancake_house_menu: PancakeHouseMenu = PancakeHouseMenu(), diner_menu: DinerMenu = DinerMenu()):
        self.pancake_house_menu = pancake_house_menu
        self.diner_menu = diner_menu

    def print_menu(self):
        print("MENU\n----\nBREAKFAST")
        print(*self.pancake_house_menu, sep='\n')
        print('\nLUNCH')
        print(*self.diner_menu, sep='\n')