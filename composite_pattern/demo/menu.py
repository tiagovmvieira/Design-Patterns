from menu_component import MenuComponent

from typing import List

class Menu(MenuComponent):
    get_name, get_description, add, get_child, remove = 'yes', 'yes', 'yes', 'yes', 'yes'
    get_price, is_vegetarian = 'no', 'no'

    def __init__(self, name: str, description: str)-> None:
        self.name = name
        self.description = description
        self.menu_components: List[MenuComponent] = []

    def add(self, menu_component: MenuComponent)-> None:
        self.menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponent)-> None:
        self.menu_components.remove(menu_component)

    def get_child(self, index: int)-> MenuComponent:
        return self.menu_components[index]

    def get_name(self)-> str:
        return self.name

    def get_description(self)-> str:
        return self.description

    def print(self)-> None:
        print("\n" + self.get_name())
        print(", " + self.get_description())
        print("---------------------")

        for menu_component in self.menu_components:
            menu_component.print()