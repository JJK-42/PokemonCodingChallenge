class Attack(object):
    def __init__(self, name, power, accuracy, element,
                 effects=[], short_info="", long_info=""):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.element = element
        self.effects = effects
        self.short_info = short_info
        if long_info == "":
            self.long_info = short_info
        else:
            self.long_info = long_info