from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 100

    @abstractmethod
    def attack(self):
        pass