from quackable import Quackable
from ducks.goose_duck import GooseDuck

class GooseDuckAdapter(Quackable):
    def __init__(self, goose: GooseDuck):
        self.goose = goose

    def quack(self):
        self.goose.honk()
