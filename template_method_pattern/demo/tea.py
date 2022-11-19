from caffeine_beverage import CaffeineBeverage, CaffeineBeverageWithHook

class Tea(CaffeineBeverage):
    def __init__(self):
        super().__init__()
        
    def _brew(self):
        print("Steeping the tea")

    def _add_condiments(self):
        print("Adding lemon")

class TeaWithUserInteraction(CaffeineBeverageWithHook):
    def __init__(self):
        super().__init__()

    def _brew(self):
        print("Steeping the tea")

    def _add_condiments(self):
        print("Adding lemon")