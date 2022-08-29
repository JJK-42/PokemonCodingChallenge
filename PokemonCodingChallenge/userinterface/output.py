# Handles output to the console
class Output(object):
    def __init__(self):
        pass


    def print_short_pokemon_info(self, pokemon):
        print(pokemon.name,
              " HP: ", pokemon.current_stats.health,
              "/", pokemon.base_stats.health)


    def print_stats(self, stats):
        print("Health: ", stats.health)
        print("Attack: ", stats.attack)
        print("Defense: ", stats.defense)
        print("Special Attack: ", stats.special_attack)
        print("Special Defense: ", stats.special_defense)
        print("Speed: ", stats.speed)
        print()


    def print_elements(self, elements):
        element_string = ""
        for element in elements:
            element_string += element.id
        print(element_string)


    def print_full_pokemon_info(self, pokemon):
        self.print_short_pokemon_info(pokemon)
        self.print_elements(pokemon.elements)
        print("Base stats:")
        self.print_stats(pokemon.base_stats)
        print("Current stats:")
        self.print_stats(pokemon.current_stats)


    def print_base_pokemon_info(self, pokemon):
        print(pokemon.name)
        self.print_elements(pokemon.elements)
        print("Stats:")
        self.print_stats(pokemon.base_stats)
        self.print_attack_list(pokemon.attack_list)



    def get_attack_stats_string(self, attack):
        return "Power: " + \
            str(attack.power) + " " + attack.element.id + \
            " Accuracy: " + str(attack.accuracy)


    def print_attack_info(self, attack):
        print(attack.name)
        print(self.get_attack_stats_string(attack))
        print(attack.long_info)
    

    def print_attack_list(self, attack_list):
        print("Attacks:")
        for attack in attack_list:
            print(attack.name, self.get_attack_stats_string(attack), attack.short_info)
        print()


    def print_combat_info(self):
        print("Opponent pokemon:")
        self.print_short_pokemon_info(self.battle.opponent_pokemon)
        print("Player pokemon:")
        self.print_short_pokemon_info(self.battle.player_pokemon)
        self.print_attack_list(self.battle.player_pokemon.attack_list)


    def print_attack_used(self, pokemon, attack):
        print(pokemon.name, " uses ", attack.name, "!")


    def print_fainted(self, pokemon):
        print(pokemon.name, " fainted!")


    def print_damage_dealt(self, pokemon, damage_dealt):
        if damage_dealt != None:
            print(pokemon.name, " takes ", damage_dealt, " damage!")
        else:
            print("The attack missed!")