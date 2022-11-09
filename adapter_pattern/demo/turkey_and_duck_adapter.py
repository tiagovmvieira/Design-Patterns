import random

from abc import ABC, abstractmethod

class Duck(ABC):
    def __init__(self):
        if self.__class__ == Duck:
            raise TypeError("Instantiating the Abstract Class")

    @abstractmethod
    def quack(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass

class MallardDuck(Duck):
    def __init__(self):
        super().__init__()

    def quack(self):
        print("Quack")

    def fly(self):
        print("I am Flying")

class Turkey(ABC):
    def __init__(self):
        if self.__class__ == Duck:
            raise TypeError("Instantiating the Abstract Class")

    @abstractmethod
    def gooble(self):
        pass

    @abstractmethod
    def fly(self):
        pass

class WildTurkey(Turkey):
    def __init__(self):
        super().__init__()

    def gooble(self):
        print("Gooble gooble")

    def fly(self):
        print("I am flying a short distance!")

class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gooble()

    def fly(self):
        i = 0
        for i in range(4):
            self.turkey.fly()
            i += 1

class DuckAdapter(Turkey):
    def __init__(self, duck: Duck):
        self.duck = duck
        self.random = random.randint(0, 30)

    def gooble(self):
        self.duck.quack()

    def fly(self):
        if self.random % 5 == 0:
            self.duck.fly()

def test_duck(duck: Duck):
    duck.quack()
    duck.fly()

def test_turkey(turkey: Turkey):
    turkey.gooble()
    turkey.fly()

if __name__ == '__main__':
    mallard_duck = MallardDuck()
    wild_turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey=wild_turkey)
    duck_adapter = DuckAdapter(duck=mallard_duck)

    print(duck_adapter.random)
    print("The Turkey says...")
    wild_turkey.gooble()
    wild_turkey.fly()

    print("The Duck says...")
    test_duck(mallard_duck)

    print("The TurkeyAdapter says...")
    test_duck(turkey_adapter)

    print("The DuckAdapter says...")
    test_turkey(duck_adapter)
