from menu_item import MenuItem
from typing import List

from collections.abc import Iterator, Iterable

class PancakeHouseMenuIterator(Iterator):
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

        return menu_item

class PancakeHouseMenu(Iterable):
    def __init__(self)-> None:
        self.menu_items : List[MenuItem] = []

        self._add_item("K&B's Pancake Breakfast", "Pancakes with scrambled eggs and toast", True, 2.99)
        self._add_item("Regular Pancake Breakfast", "Pancakes with fried eggs, sausage", False, 2.99)
        self._add_item("Blueberry Pancakes", "Pancakes made with fresh blueberries", True, 3.49)
        self._add_item("Waffles", "Waffles with you choice of blueberries or strawberries", True, 3.59)

    def _add_item(self, name: str, description: str, vegetarian: bool, price: float)-> None:
        menu_item : MenuItem = MenuItem(name, description, vegetarian, price)
        self.menu_items.append(menu_item)

    def __iter__(self)-> PancakeHouseMenuIterator:
        return PancakeHouseMenuIterator(self.menu_items)

    def get_reverse_iterator(self)-> PancakeHouseMenuIterator:
        return PancakeHouseMenuIterator(self.menu_items, True)

    