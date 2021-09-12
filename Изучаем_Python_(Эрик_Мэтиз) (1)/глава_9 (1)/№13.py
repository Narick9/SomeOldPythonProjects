
from random import randint


class Die():
    """Кубик, с которым можно испытать удачу"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Бросок кубика"""
        result = randint(1, self.sides)
        print("Dropped " + str(result))


die_6 = Die()
die_10 = Die(sides=10)
die_20 = Die(sides=20)

for die in (die_6, die_10, die_20):
    print(str(die.sides) + "-sides cube:")
    
    for _ in range(10):
        print(end="\t")
        die.roll_die()
    print()
