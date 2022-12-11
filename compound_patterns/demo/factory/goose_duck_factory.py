from ducks.goose_duck import GooseDuck
from adapter.goose_adapter import GooseDuckAdapter

from quackable import Quackable

class GooseDuckFactory:
    def __init__(self)-> None:
        pass

    def create_goose_duck(self)-> Quackable:
        return GooseDuckAdapter(GooseDuck())