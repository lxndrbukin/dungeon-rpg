from abc import ABC, abstractmethod

class Character():
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 100
    @property
    def name(self):
        return self._name
    @property
    def health(self):
        return self._health
    def take_damage(self, damage):
        self._health -= damage

class Class(ABC):
    @abstractmethod
    def attack(self, target, weapon):
        pass

class Knight(Character, Class):
    def attack(self, target, weapon):
        damage = 10
        target.take_damage(damage)
        return f"{self.name} attacks {target.name} with his {weapon} and deals {damage} damage!\n{target.name}: {target.health} health left."