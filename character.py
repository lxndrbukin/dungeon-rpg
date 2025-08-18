from abc import ABC, abstractmethod

class Character:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 100
        self._weapon = None
    @property
    def name(self):
        return self._name
    @property
    def health(self):
        return self._health
    @health.setter
    def health(self, action):
        if action["type"] == "damage":
            self._health -= action["value"]
        elif action["type"] == "heal":
            self._health += action["value"]
    @property
    def weapon(self):
        return self._weapon
    @weapon.setter
    def weapon(self, new_weapon):
        self._weapon = new_weapon
    def take_damage(self, damage):
        self._health -= damage

class Class(ABC, Character):
    def attack(self, target):
        damage = 10
        target.take_damage(damage)
        return f"{self.name} attacks {target.name} with his {self.weapon} and deals {damage} damage!\n{target.name}: {target.health} health left."
    @abstractmethod
    def strong_attack(self, target):
        pass

class Knight(Class):
    def strong_attack(self, target):
        damage = 25
        used_mana = 25


# class Wizard(Class):
