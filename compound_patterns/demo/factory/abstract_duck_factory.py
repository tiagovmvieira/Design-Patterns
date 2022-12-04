from abc import ABC, abstractmethod

class AbstractDuckFactory(ABC):
    @abstractmethod
    def create_mallard_duck(self)-> None:
        pass

    @abstractmethod
    def create_red_head_duck(self)-> None:
        pass

    @abstractmethod
    def create_duck_call(self)-> None:
        pass

    @abstractmethod
    def create_rubber_duck(self)-> None:
        pass