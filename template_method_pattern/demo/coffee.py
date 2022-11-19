from caffeine_beverage import CaffeineBeverage, CaffeineBeverageWithHook

class Coffee(CaffeineBeverage):
    def __init__(self):
        super().__init__()

    def _brew(self):
        print("Dripping Coffee through filter")

    def _add_condiments(self):
        print("Adding Sugar and Milk")