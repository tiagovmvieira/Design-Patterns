from diner_menu import DinerMenu, DinerMenuIterator
from pancake_house_menu import PancakeHouseMenu, PancakeHouseMenuIterator

class Waitress:
    def __init__(self, pancake_house_menu: PancakeHouseMenu = PancakeHouseMenu(), diner_menu: DinerMenu = DinerMenu()):
        self.pancake_house_menu = pancake_house_menu
        self.diner_menu = diner_menu

    def print_menu(self):
        print("MENU\n----\nBREAKFAST")
        self.print_detailed_menu(PancakeHouseMenuIterator(self.pancake_house_menu.menu_items))
        print('\nLUNCH')
        self.print_detailed_menu(DinerMenuIterator(self.diner_menu.menu_items))

    def print_detailed_menu(self, iterator):
        for menu_item in iterator:
            print(menu_item.get_name() + ", " + str(menu_item.get_price()) + " -- " + menu_item.get_description())