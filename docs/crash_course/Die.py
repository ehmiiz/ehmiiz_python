"""
A class that tries to represent a real world dice.
"""
from random import choice

class Die:
    def __init__(self, sides: int):
        sides += 1
        self.sides = range(1,sides)
    
    def roll_die(self):
        rolling = choice(self.sides)
        print(f"Die rolled a {rolling}")
    
    def show_all_sides(self):
        print("Going through all sides of the die:")
        for side in self.sides:
            print(side)


my_tensided_die = Die(sides=6)

my_tensided_die.roll_die()

my_tensided_die.show_all_sides()