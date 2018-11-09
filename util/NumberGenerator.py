from random import randint

class NumberGenerator:
    def generate(self):
        chance = randint(0, 9)
        if chance == 9:
            return 4
        else:
            return 2


