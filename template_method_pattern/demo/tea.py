from caffeine_beverage import CaffeineBeverage, CaffeineBeverageWithHook
from termcolor import colored

class Tea(CaffeineBeverage):
    def __init__(self):
        super().__init__()
        
    def _brew(self):
        print("Steeping the tea")

    def _add_condiments(self):
        print("Adding lemon")

class TeaWithHook(CaffeineBeverageWithHook):
    def __init__(self):
        super().__init__()

    def _brew(self):
        print("Steeping the tea")

    def _add_condiments(self):
        print("Adding lemon")

    def _get_user_input(self)-> str:
        user_answer = None
        user_answer = str(input(colored("Would you like lemon with your tea (y/n)? ", "red")))

        return user_answer

    def _customer_wants_condiments(self) -> bool:
        self.user_answer: str = self._get_user_input()

        if self.user_answer.lower().startswith("y"):
            return True
        else:
            return False