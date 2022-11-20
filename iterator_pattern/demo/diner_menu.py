from menu_item import MenuItem
from typing import List, Final

from collections.abc import Iterator, Iterable

class DinerMenuIterator(Iterator):
    def __init__(self, menu_items: List[MenuItem], reverse: bool = False)-> None:
        self.menu_items = menu_items
        self.reverse = reverse
        self.position = -1 if reverse else 0

    def __next__(self)-> MenuItem:
        try:
            menu_item = self.menu_items[self.position] 
            self.position += -1 if self.reverse else 1
        except IndexError:
            raise StopIteration()

        if menu_item is not None:
            return menu_item
        else:
            raise StopIteration()

class DinerMenu:
    def __init__(self):
        self.MAX_ITEMS: Final[int] = 6
        self.number_of_items: int = 0
        self.menu_items: List[MenuItem] = [None] * self.MAX_ITEMS

        self._add_item("Vegetarian BLT", "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self._add_item("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self._add_item("Soup of the day", "Soup of the day, with a side of potato salad", False, 3.29)
        self._add_item("Hotdog", "A hot dog, with sauerkraut, relish, onions, topped with cheese", False, 3.05)

        self.position: int = 0

    def _add_item(self, name: str, description: str, vegetarian: bool, price: float):
        menu_item: MenuItem = MenuItem(name, description, vegetarian, price)

        if self.number_of_items > self.MAX_ITEMS:
            print("Sorry menu is full! Can't add item to menu")
        else:
            self.menu_items[self.number_of_items] = menu_item
            self.number_of_items += 1

    def __iter__(self)-> DinerMenuIterator:
        return DinerMenuIterator(self.menu_items)

    def get_reverse_iterator(self)-> DinerMenuIterator:
        return DinerMenuIterator(self.menu_items, True)