from caffeine_beverage import CaffeineBeverage, CaffeineBeverageWithHook
from termcolor import colored

class Coffee(CaffeineBeverage):
    def __init__(self):
        super().__init__()

    def _brew(self):
        print("Dripping Coffee through filter")

    def _add_condiments(self):
        print("Adding Sugar and Milk")

class CoffeeWithHook(CaffeineBeverageWithHook):
    def __init__(self):
        super().__init__()

    def _brew(self):
        print("Dripping Coffee through filter")

    def _add_condiments(self):
        print("Adding Sugar and Milk")

    def _get_user_input(self)-> str:
        user_answer = None
        user_answer = str(input(colored("Would you like milk and sugar with your coffee (y/n)? ", "red")))

        return user_answer

    def _customer_wants_condiments(self) -> bool:
        self.user_answer: str = self._get_user_input()

        if self.user_answer.lower().startswith("y"):
            return True
        else:
            return False
