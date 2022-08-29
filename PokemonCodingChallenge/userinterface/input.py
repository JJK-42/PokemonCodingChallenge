# Handles command line input
class Input(object):
    def __init__(self, view):
        self.view = view


    def parse_attack_info_input(self, user_input, pokemon):
        attack_name = user_input.replace(" info", "").replace("info", "")
        info_attack = pokemon.get_attack(attack_name)
        if info_attack != None:
            self.view.print_attack_info(info_attack)
        else:
            print("That attack does not exist!")


    def parse_attack_input(self, user_input, pokemon):
        attack = None

        if "pokemon" in user_input:
            pokemon = self.battle.player_pokemon
            self.view.print_full_pokemon_info(pokemon)
        elif "info" in user_input:
            self.parse_attack_info_input(user_input, pokemon)
        else:
            attack = pokemon.get_attack(user_input)

        return attack


    def input_attack(self, pokemon):
        user_input = input("Input next attack: ")
        return self.parse_attack_input(user_input, pokemon)


    def get_next_attack(self, pokemon):
        print("What do you want to do?")
        print("- Type the name of the attack to use it")
        print("- Type 'pokemon' to view detailed statistics of your pokemon")
        print("- Type '<attack name> info' to see",
              " detailed information of your attacks")
        self.view.print_attack_list(pokemon.attack_list)
        attack = None
        while attack == None:
            attack = self.input_attack(pokemon)
        return attack



