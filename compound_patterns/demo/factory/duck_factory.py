from abstract_duck_factory import AbstractDuckFactory
from ducks.mallard_duck import MallardDuck
from ducks.red_head_duck import RedHeadDuck
from ducks.duck_call import DuckCall
from ducks.rubber_duck import RubberDuck

from quackable import Quackable

class DuckFactory(AbstractDuckFactory):
    def __init__(self)-> None:
        pass

    def create_mallard_duck(self)->Quackable:
        return MallardDuck()

    def create_red_head_duck(self)->Quackable:
        return RedHeadDuck()

    def create_duck_call(self)->Quackable:
        return DuckCall()

    def create_rubber_duck(self)->Quackable:
        return RubberDuck()