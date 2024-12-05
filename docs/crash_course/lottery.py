"""A script that mimics how a basic lottery works."""
from random import choice

# Declare variables
list = [5, 17, 25, 19, 12, 19, 95, 8, 18, 3, "d", "a", "f", "e", "l"]
active = True
result = []
my_ticket = [5, "d", 18, 95]
counter = 1

# Lottery loop
while active:
    if len(result) == 4:
        if my_ticket == result:
            print(f"Winner, your ticket {my_ticket}, winning ticket {result}\nMagic try number {counter}")
            active = False
        else:
            print(f"On try number {counter}: {my_ticket} is not {result}")
            result = []
    else:
        result.append(choice(list))
    counter += 1