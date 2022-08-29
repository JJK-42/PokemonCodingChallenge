from userinterface.input import Input
from userinterface.output import Output
from backend import attack, element, pokemon, stats, battlesetup


_FLAMETHROWER_NAME = "Flamethrower"
_FIRE_BLAST_NAME = "Fire Blast"
_WING_ATTACK_NAME = "Wing Attack"
_WILL_O_WISP_NAME = "Will-o-wisp"
_SURF_NAME = "Surf"
_HYDRO_PUMP_NAME = "Hydro Pump"
_BODY_SLAM_NAME = "Body Slam"
_REST_NAME = "Rest"
_RAZOR_LEAF_NAME = "Razor Leaf"
_TOXIC_NAME = "Toxic"
_EARTH_QUAKE_NAME = "Earth Quake"
_CROSS_CHOP_NAME = "Cross Chop"
_FIRE_PUNCH_NAME = "Fire Punch"
_AGILITY_NAME = "Agility"
_SLUDGE_BOMB_NAME = "Sludge Bomb"
_STRENGTH_NAME = "Strength"
_DETECT_NAME = "Detect"

_CHARIZARD_NAME = "Charizard"
_BLASTOISE_NAME = "Blastoise"
_VENUSAUR_NAME = "Venusaur"
_HITMONCHAN_NAME = "Hitmonchan"
_NIDOKING_NAME = "Nidoking"
_PIDGEOT_NAME = "Pidgeot"


def generate_default_attacks():
    attack_dict = {}

    attack_dict[_FLAMETHROWER_NAME] = attack.Attack(
        _FLAMETHROWER_NAME, 95, 100, element.FIRE,
    )

    attack_dict[_FIRE_BLAST_NAME] = attack.Attack(
        _FIRE_BLAST_NAME, 120, 85, element.FIRE,
    )

    attack_dict[_WING_ATTACK_NAME] = attack.Attack(
        _WING_ATTACK_NAME, 65, 100, element.FLYING,
    )
    
    attack_dict[_WILL_O_WISP_NAME] = attack.Attack(
        _WILL_O_WISP_NAME, 0, 90, element.FIRE,
        short_info="Causes Burn Status",
        long_info="Causes Burn Status, \
        dealing damage over time and lowering attack"
    )

    attack_dict[_SURF_NAME] = attack.Attack(
        _SURF_NAME, 95, 100, element.WATER,
    )

    attack_dict[_HYDRO_PUMP_NAME] = attack.Attack(
        _HYDRO_PUMP_NAME, 120, 85, element.WATER,
    )
    
    attack_dict[_BODY_SLAM_NAME] = attack.Attack(
        _BODY_SLAM_NAME, 80, 100, element.NORMAL,
        short_info="May cause Paralysis",
        long_info="30% chance to cause Paralysis status"
    )
    
    attack_dict[_REST_NAME] = attack.Attack(
        _REST_NAME, 0, 100, element.NORMAL,
        short_info="Heal, but fall asleep",
        long_info="Fully heals the user but causes them to sleep for 2 turns"
    )

    attack_dict[_RAZOR_LEAF_NAME] = attack.Attack(
        _RAZOR_LEAF_NAME, 75, 95, element.GRASS,
    )
    
    attack_dict[_TOXIC_NAME] = attack.Attack(
        _TOXIC_NAME, 0, 90, element.POISON,
        short_info="Causes Poison status",
        long_info="Causes Poison status, dealing increasing damage over time"
    )

    attack_dict[_EARTH_QUAKE_NAME] = attack.Attack(
        _EARTH_QUAKE_NAME, 100, 100, element.GROUND,
    )

    attack_dict[_CROSS_CHOP_NAME] = attack.Attack(
        _CROSS_CHOP_NAME, 100, 90, element.FIGHTING,
    )

    attack_dict[_FIRE_PUNCH_NAME] = attack.Attack(
        _FIRE_PUNCH_NAME, 75, 95, element.FIRE,
    )

    attack_dict[_AGILITY_NAME] = attack.Attack(
        _AGILITY_NAME, 0, 100, element.NORMAL,
        short_info="Doubles speed",
    )

    attack_dict[_SLUDGE_BOMB_NAME] = attack.Attack(
        _SLUDGE_BOMB_NAME, 80, 100, element.POISON,
    )

    attack_dict[_STRENGTH_NAME] = attack.Attack(
        _STRENGTH_NAME, 90, 100, element.NORMAL,
    )

    attack_dict[_DETECT_NAME] = attack.Attack(
        _DETECT_NAME, 0, 100, element.FIGHTING,
        short_info="Protects the user",
        long_info="Protects the user from the next attack"
    )

    return attack_dict


def generate_default_pokemon():
    pokemon_dict = {}
    attack_dict = generate_default_attacks()

    pokemon_dict[_CHARIZARD_NAME] = pokemon.Pokemon(_CHARIZARD_NAME,
                        stats.Stats(298, 183, 192, 317, 206, 328),
                        (element.FIRE, element.FLYING),
                        [attack_dict[_FLAMETHROWER_NAME],
                         attack_dict[_FIRE_BLAST_NAME],
                         attack_dict[_WING_ATTACK_NAME],
                         attack_dict[_WILL_O_WISP_NAME]]
    )

    pokemon_dict[_BLASTOISE_NAME] = pokemon.Pokemon(_BLASTOISE_NAME,
                        stats.Stats(362, 202, 236, 295, 247, 172),
                        (element.WATER,),
                        [attack_dict[_SURF_NAME],
                         attack_dict[_HYDRO_PUMP_NAME],
                         attack_dict[_BODY_SLAM_NAME],
                         attack_dict[_REST_NAME]]
    )

    pokemon_dict[_VENUSAUR_NAME] = pokemon.Pokemon(_VENUSAUR_NAME,
                        stats.Stats(364, 200, 181, 328, 237, 196),
                        (element.GRASS, element.POISON),
                        [attack_dict[_RAZOR_LEAF_NAME],
                         attack_dict[_BODY_SLAM_NAME],
                         attack_dict[_TOXIC_NAME],
                         attack_dict[_EARTH_QUAKE_NAME]]
    )

    pokemon_dict[_HITMONCHAN_NAME] = pokemon.Pokemon(_HITMONCHAN_NAME,
                        stats.Stats(241, 309, 194, 95, 257, 276),
                        (element.FIGHTING,),
                        [attack_dict[_CROSS_CHOP_NAME],
                         attack_dict[_FIRE_PUNCH_NAME],
                         attack_dict[_BODY_SLAM_NAME],
                         attack_dict[_AGILITY_NAME]]
    )

    pokemon_dict[_NIDOKING_NAME] = pokemon.Pokemon(_NIDOKING_NAME,
                        stats.Stats(366, 333, 191, 206, 167, 206),
                        (element.GROUND, element.POISON),
                        [attack_dict[_EARTH_QUAKE_NAME],
                         attack_dict[_SLUDGE_BOMB_NAME],
                         attack_dict[_STRENGTH_NAME],
                         attack_dict[_SURF_NAME]]
    )

    pokemon_dict[_PIDGEOT_NAME] = pokemon.Pokemon(_PIDGEOT_NAME,
                        stats.Stats(370, 284, 186, 158, 176, 239),
                        (element.FLYING, element.NORMAL),
                        [attack_dict[_WING_ATTACK_NAME],
                         attack_dict[_AGILITY_NAME],
                         attack_dict[_BODY_SLAM_NAME],
                         attack_dict[_DETECT_NAME]]
    )

    return pokemon_dict


def main():
    pokemon_dict = generate_default_pokemon()
    UI_output = Output()
    UI_controller = Input(UI_output)
    setup = battlesetup.BattleSetup(UI_output, UI_controller)
    battle = setup.create_battle(pokemon_dict)
    battle.start_battle(UI_output, UI_controller)


if __name__ == "__main__":
    main()
