from abc import ABC, abstractmethod

class MenuComponent(ABC):
    @abstractmethod
    def __init__(self)-> None:
        if self.__class__ == MenuComponent:
            raise TypeError("Instantiating the Abstract Class")

    @property
    @abstractmethod
    def add(self, menu_component)-> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def remove(self, menu_component)-> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_child(self, index: int)-> None:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_name(self)-> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_description(self)-> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def get_price(self)-> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_vegetarian(self)-> bool:
        raise NotImplementedError

    def print(self)-> None:
        pass