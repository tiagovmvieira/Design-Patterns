from menu import Menu
from menu_item import MenuItem
from menu_component import MenuComponent

from waitress import Waitress

from termcolor import colored

if __name__ == '__main__':
    print(colored('------------------ COMPOSITE PATTERN ----------------', 'white'))
    pancake_house_menu: MenuComponent = Menu("PANCAKE HOUSE MENU", "Breakfast")
    diner_menu: MenuComponent = Menu("DINER MENU", "Lunch")
    cafe_menu: MenuComponent = Menu("CAFE MENU", "Dinner")
    dessert_menu: MenuComponent = Menu("DESSERT MENU", "Dessert of course!")

    all_menus: MenuComponent = Menu("ALL MENUS", "All menus combined")

    all_menus.add(pancake_house_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)

    diner_menu.add(MenuItem(
        "Pasta",
        "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
        True,
        3.89
    ))

    diner_menu.add(dessert_menu)

    dessert_menu.add(MenuItem(
        "Apple Pie",
        "Apple Pie with a flakey crust, topped with vanilla ice cream",
        True,
        1.59
    ))

    waitress: Waitress = Waitress(all_menus)
    waitress.print_menu()

