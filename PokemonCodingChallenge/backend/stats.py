# Holds statistics of a pokemon
class Stats(object):
    def __init__(self, health, attack, defense,
                 special_attack, special_defense, speed):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def copy(self):
        return Stats(self.health, self.attack, self.defense,
                          self.special_attack, self.special_defense,
                          self.speed)
