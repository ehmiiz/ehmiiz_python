"""Tries to represent a real world lottery"""
from random import choice

class lottery:
    """The lottery itself"""
    def __init__(self, lottery_name, current_jackpot):
        self.list = [5, 17, 25, 19, 12, 19, 95, 8, 18, 3, "d", "a", "f", "e", "l"]
        self.lottery_name = lottery_name
        self.current_jackpot = current_jackpot
        
    def run_the_lottery(self, my_ticket):
        counter = 1
        result = []
        active = True
        while active:
            if len(result) == 4:
                if my_ticket == result:
                    print(f"Winner, your ticket {my_ticket}, winning ticket {result}\nMagic try number {counter}")
                    active = False
                else:
                    print(f"On try number {counter}: {my_ticket} is not {result}")
                    result = []
            else:
                result.append(choice(self.list))
                counter += 1