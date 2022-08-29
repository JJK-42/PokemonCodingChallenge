class Element(object):
    _FIRE_ID = "Fire"
    _GRASS_ID = "Grass"
    _WATER_ID = "Water"
    _POISON_ID = "Poison"
    _FLYING_ID = "Flying"
    _GROUND_ID = "Ground"
    _NORMAL_ID = "Normal"
    _FIGHTING_ID = "Fighting"

    _PHYSICAL = True
    _SPECIAL = False
    

    def __init__(self, is_physical, effectiveness, element_id):
        self.is_physical = is_physical
        self.effectiveness = effectiveness
        self.id = element_id


    def resistance_to(self, element):
        return element.effectiveness[self.id]
    

FIRE = Element(
    Element._SPECIAL,
    {
        Element._FIRE_ID: 0.5,
        Element._GRASS_ID: 2,
        Element._WATER_ID: 0.5,
        Element._POISON_ID: 1,
        Element._FLYING_ID: 1,
        Element._GROUND_ID: 0.5,
        Element._NORMAL_ID: 1,
        Element._FIGHTING_ID: 1,
    },
    Element._FIRE_ID
)


GRASS = Element(
    Element._SPECIAL,
    {
        Element._FIRE_ID: 0.5,
        Element._GRASS_ID: 0.5,
        Element._WATER_ID: 2,
        Element._POISON_ID: 1,
        Element._FLYING_ID: 1,
        Element._GROUND_ID: 2,
        Element._NORMAL_ID: 1,
        Element._FIGHTING_ID: 1,
    },
    Element._GRASS_ID
)


WATER = Element(
    Element._SPECIAL,
    {
        Element._FIRE_ID: 2,
        Element._GRASS_ID: 0.5,
        Element._WATER_ID: 0.5,
        Element._POISON_ID: 1,
        Element._FLYING_ID: 1,
        Element._GROUND_ID: 2,
        Element._NORMAL_ID: 1,
        Element._FIGHTING_ID: 1,
    },
    Element._WATER_ID
)


POISON = Element(
    Element._PHYSICAL,
    {
        Element._FIRE_ID: 1,
        Element._GRASS_ID: 2,
        Element._WATER_ID: 1,
        Element._POISON_ID: 0.5,
        Element._FLYING_ID: 1,
        Element._GROUND_ID: 0.5,
        Element._NORMAL_ID: 1,
        Element._FIGHTING_ID: 1,
    },
    Element._POISON_ID
)


FLYING = Element(
    Element._PHYSICAL,
    {
        Element._FIRE_ID: 1,
        Element._GRASS_ID: 2,
        Element._WATER_ID: 1,
        Element._POISON_ID: 1,
        Element._FLYING_ID: 1,
        Element._GROUND_ID: 1,
        Element._NORMAL_ID: 1,
        Element._FIGHTING_ID: 2,
    },
    Element._FLYING_ID
)


GROUND = Element(
    Element._PHYSICAL,
    {
        Element._FIRE_ID: 2,
        Element._GRASS_ID: 0.5,
        Element._WATER_ID: 1,
        Element._POISON_ID: 2,
        Element._FLYING_ID: 0,
        Element._GROUND_ID: 1,
        Element._NORMAL_ID: 1,
        Element._FIGHTING_ID: 1,
    },
    Element._GROUND_ID
)


NORMAL = Element(
    Element._PHYSICAL,
    {
        Element._FIRE_ID: 1,
        Element._GRASS_ID: 1,
        Element._WATER_ID: 1,
        Element._POISON_ID: 1,
        Element._FLYING_ID: 1,
        Element._GROUND_ID: 1,
        Element._NORMAL_ID: 1,
        Element._FIGHTING_ID: 1,
    },
    Element._NORMAL_ID
)


FIGHTING = Element(
    Element._SPECIAL,
    {
        Element._FIRE_ID: 1,
        Element._GRASS_ID: 1,
        Element._WATER_ID: 1,
        Element._POISON_ID: 0.5,
        Element._FLYING_ID: 0.5,
        Element._GROUND_ID: 1,
        Element._NORMAL_ID: 2,
        Element._FIGHTING_ID: 1,
    },
    Element._FIGHTING_ID
)