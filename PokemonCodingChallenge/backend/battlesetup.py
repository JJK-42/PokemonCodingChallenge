from .battle import Battle

class BattleSetup(object):
    def __init__(self, view, controller):
        self.view = view
        self.controller = controller


    def parse_pokemon_input(self, pokemon_dict):
        user_input = input()
        pokemon_name = user_input.split()[0]
        pokemon = None

        if pokemon_name in pokemon_dict:
            pokemon = pokemon_dict[pokemon_name]
        else:
            print("That pokemon does not exist")
            return None

        if "info" in user_input:
            self.view.print_base_pokemon_info(pokemon)
            return None
        else:
            return pokemon


    def list_pokemon(self, pokemon_dict):
        for pokemon_name in pokemon_dict:
            print(pokemon_name)
        print()


    def select_pokemon(self, pokemon_dict):
        pokemon = None
        while pokemon == None:
            print("Type the name to select the pokemon")
            print("Type 'info' after the name for detailed info")
            pokemon = self.parse_pokemon_input(pokemon_dict)
        print()
        return pokemon.copy()


    def create_battle(self, pokemon_dict):
        player_pokemon = None
        opponent_pokemon = None
        while player_pokemon == None or opponent_pokemon == None:
            self.list_pokemon(pokemon_dict)
            print("Select the pokemon you would like to use")
            player_pokemon = self.select_pokemon(pokemon_dict)
            print("Select the pokemon you would like to fight against")
            opponent_pokemon = self.select_pokemon(pokemon_dict)

        return Battle(player_pokemon, opponent_pokemon, self.view)

