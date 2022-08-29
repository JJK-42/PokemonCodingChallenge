import random

class Pokemon(object):
    SAME_TYPE_ATTACK_BONUS = 1.5


    def __init__(self, name, base_stats, elements, attack_list):
        self.name = name
        self.base_stats = base_stats
        self.current_stats = base_stats.copy()
        self.elements = elements
        self.attack_list = attack_list
        self.active_statuses = []


    def is_alive(self):
        return self.current_stats.health > 0


    def copy(self):
        return Pokemon(self.name, self.base_stats.copy(),
                       self.elements, self.attack_list)


    def trigger_statuses(self):
        for status in self.active_statuses:
            status.trigger(self)


    def compute_damage_taken(self, power, attack_element):
        resistance = 1
        for element in self.elements:
            resistance *= element.resistance_to(attack_element)
        damage = power * resistance
        
        if element.is_physical:
            damage /= self.current_stats.defense
        else:
            damage /= self.current_stats.special_defense

        return damage


    def apply_statuses(self, effects):
        for effect in effects:
            if effect not in self.active_statuses:
                self.active_statuses.append(effect)


    def take_damage(self, damage):
        if damage > self.current_stats.health:
            self.current_stats.health = 0
        else:
            self.current_stats.health -= damage


    def take_hit(self, power, element, effect):
        damage = self.compute_damage_taken(power, element)
        self.take_damage(damage)
        self.apply_statuses(effect)
        return damage


    def get_attack(self, attack_name):
        for attack in self.attack_list:
            if attack_name == attack.name:
                return attack

        return None


    def compute_attack_power(self, attack):
        power = attack.power

        if attack.element in self.elements:
            power *= Pokemon.SAME_TYPE_ATTACK_BONUS

        if attack.element.is_physical:
            power *= self.current_stats.attack
        else:
            power *= self.current_stats.special_attack

        return power


    def use_attack(self, attack, target):
        if attack not in self.attack_list:
            return
        
        power = self.compute_attack_power(attack)

        if attack.accuracy > random.randrange(0, 100):
            return target.take_hit(power, attack.element, attack.effects)
        else:
            return None


