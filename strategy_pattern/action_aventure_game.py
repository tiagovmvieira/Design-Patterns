from __future__ import annotations
from abc import ABC, abstractmethod
from termcolor import colored

class Character():
    def __init__(self, weapon_behaviour: WeaponBehaviour):
        self.weapon_behaviour = weapon_behaviour

    def display()-> str:
        pass

    def set_weapon(self, weapon_behaviour: WeaponBehaviour):
        self.weapon_behaviour = weapon_behaviour

    def fight(self):
        return self.weapon_behaviour.use_weapon(self)

class WeaponBehaviour(ABC):
    @abstractmethod
    def use_weapon(self):
        pass

class SwordBehaviour(WeaponBehaviour):
    def __init__(self):
        pass

    def use_weapon(self)-> str:
        return 'Implements swinging a sword'

class KnifeBehaviour(WeaponBehaviour):
    def __init__(self):
        pass

    def use_weapon(self)-> str:
        return 'Implements cutting with a knife'

class BowAndArrowBehaviour(WeaponBehaviour):
    def __init__(self):
        pass

    def use_weapon(self)-> str:
        return 'Implements shooting an arrow with a bow'

class AxeBehaviour(WeaponBehaviour):
    def __init__(self):
        pass

    def use_weapon(self)-> str:
        return 'Implements chopping with an axe'

class King(Character):
    def __init__(self, weapon_behaviour):
        super().__init__(weapon_behaviour)

    def display(self)-> str:
        return 'I am a King!'

class Queen(Character):
    def __init__(self, weapon_behaviour):
        super().__init__(weapon_behaviour)

    def display(self)-> str:
        return 'I am a Queen!'

class Knight(Character):
    def __init__(self, weapon_behaviour):
        super().__init__(weapon_behaviour)

    def display(self)-> str:
        return 'I am a Knight!'

class Troll(Character):
    def __init__(self, weapon_behaviour):
        super().__init__(weapon_behaviour)

    def display(self)-> str:
        return 'I am a Troll!'

if __name__ == '__main__':
    print(colored('------------------------ KING -----------------------', 'blue'))
    king = King(AxeBehaviour)
    print(king.display())
    print(king.fight())
    
    print(colored('----------------------- QUEEN -----------------------', 'red'))
    queen = Queen(BowAndArrowBehaviour)
    print(queen.display())
    print(queen.fight())

    print(colored('----------------------- KNIGHT ----------------------', 'green'))
    knight = Knight(SwordBehaviour)
    print(knight.display())
    print(knight.fight())

    print(colored('----------------------- TROLL -----------------------', 'yellow'))
    troll = Troll(SwordBehaviour)
    print(troll.display())
    troll.set_weapon(KnifeBehaviour)
    print(troll.fight())
    