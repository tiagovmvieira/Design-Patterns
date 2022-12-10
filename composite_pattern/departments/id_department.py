from abc import ABC, abstractmethod

class IDepartment(ABC):
    @abstractmethod
    def __init__(self, no_employees: int)-> None:
        if self.__class__ == IDepartment:
            raise TypeError("Instantiating the Abstract Class")
        self.no_employees = no_employees

    @abstractmethod
    def print_department(self)-> None:
        pass
