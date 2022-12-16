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

    pancake_house_menu.add((MenuItem(
        "K&B's Pancake Breakfast",
        "Pancakes with scrambled eggs and toast",
        True,
        2.99
    )))

    pancake_house_menu.add((MenuItem(
        "Regular Pancake Breakfast",
        "Pancakes with fried eggs, sausage",
        False,
        2.99
    )))

    pancake_house_menu.add((MenuItem(
        "Blueberry Pancakes",
        "Pancakes made with fresh blueberries, and blueberry syrup",
        True,
        3.49
    )))

    pancake_house_menu.add((MenuItem(
        "Waffles",
        "Waffles with your choice of blueberries or strawberries",
        True,
        3.59
    )))

    diner_menu.add(MenuItem(
        "Vegetarian BLT",
        "(Fakin') Bacon with lettuce & tomato on whole wheat",
        True,
        2.99
    ))

    diner_menu.add(MenuItem(
        "BLT",
        "Bacon with lettuce & tomato on whole wheat",
        False,
        2.99
    ))

    diner_menu.add(MenuItem(
        "Soup of the day",
        "A bowl of the soup of the day, with a side of potato salad",
        False,
        3.29
    ))

    diner_menu.add(MenuItem(
        "Hot Dog",
        "A hot dog, with sauerkraut, relish, onions, topped with cheese",
        False,
        3.05
    ))

    diner_menu.add(MenuItem(
        "Steamed Veggies and Brown Rice",
        "Steamed vegetables over brown rice",
        True,
        3.99
    ))

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

    dessert_menu.add(MenuItem(
        "Cheesecake",
        "Creamy New York cheesecake, with a chocolate graham crust",
        True,
        1.99
    ))

    dessert_menu.add(MenuItem(
        "Sorbet",
        "A scoop of raspberry and a coop of lime",
        True,
        1.89
    ))

    cafe_menu.add(MenuItem(
        "Veggie Burguer and Air Fries",
        "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
        True,
        3.99
    ))

    cafe_menu.add(MenuItem(
        "Soup of the day",
        "A cup of the soup of the day, with a side salad",
        False,
        3.69
    ))

    cafe_menu.add(MenuItem(
        "Burrito",
        "A large burrito, with whole pinto beans, salsa, guacamole",
        True,
        4.29
    ))

    waitress: Waitress = Waitress(all_menus)
    waitress.print_menu()

