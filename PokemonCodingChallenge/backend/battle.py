import random

class Battle(object):
    def __init__(self, player_pokemon, opponent_pokemon, view):
        self.player_pokemon = player_pokemon
        self.opponent_pokemon = opponent_pokemon
        self.view = view
        

    def do_turn(self, player_attack, opponent_attack):
        player_speed = self.player_pokemon.current_stats.speed
        opponent_speed = self.opponent_pokemon.current_stats.speed

        first_pokemon = self.opponent_pokemon
        first_attack = opponent_attack
        second_pokemon = self.player_pokemon
        second_attack = player_attack

        if player_speed > opponent_speed:
            first_pokemon = self.player_pokemon
            first_attack = player_attack
            second_pokemon = self.opponent_pokemon
            second_attack = opponent_attack
            
        self.view.print_attack_used(first_pokemon, first_attack)
        first_damage = first_pokemon.use_attack(first_attack, second_pokemon)
        self.view.print_damage_dealt(second_pokemon, first_damage)

        if not second_pokemon.is_alive():
            self.view.print_fainted(second_pokemon)
            return

        self.view.print_attack_used(second_pokemon, second_attack)
        second_damage = second_pokemon.use_attack(second_attack,
                                                  first_pokemon)
        self.view.print_damage_dealt(first_pokemon, second_damage)

        self.player_pokemon.trigger_statuses()
        self.opponent_pokemon.trigger_statuses()


    def compute_attack(self):
        return random.choice(self.opponent_pokemon.attack_list)


    def end_battle(self):
        if self.player_pokemon.is_alive():
            print("You win!")
        else:
            print("You lose...")


    def start_battle(self, view, controller):
        while (self.player_pokemon.is_alive() and
               self.opponent_pokemon.is_alive()):
            view.print_short_pokemon_info(self.player_pokemon)
            print("VS")
            view.print_short_pokemon_info(self.opponent_pokemon)
            print()
            player_attack = controller.get_next_attack(self.player_pokemon)
            opponent_attack = self.compute_attack()
            self.do_turn(player_attack, opponent_attack)
        
        self.end_battle()