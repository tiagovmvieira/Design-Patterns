from menu_component import MenuComponent

class MenuItem(MenuComponent):
    get_name, get_description, get_price, is_vegetarian = 'yes', 'yes', 'yes', 'yes'
    add, get_child, remove = 'no', 'no', 'no'

    def __init__(self, name: str, description: str, vegetarian: bool, price: float):
        super().__init__()
        self.name=name
        self.description=description
        self.vegetarian=vegetarian
        self.price=price

    def get_name(self)-> str:
        return self.name

    def get_description(self)-> str:
        return self.description

    def get_price(self)-> float:
        return self.price

    def is_vegetarian(self) -> bool:
        return self.vegetarian

    def print(self):
        print(" ", self.get_name(), "(v)" if self.is_vegetarian() else "", ", " + str(self.get_price()), "\n     -- " + self.get_description())