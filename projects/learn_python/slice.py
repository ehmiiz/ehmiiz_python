"""

    1. First, return a slice of the champions list that starts with the third champion and goes to the end of the list.
    2. Next, return a slice of the champions list that starts at the beginning of the list and ends with the third champion from the end (inclusive).
    3. Last, return a slice of the champions list that only includes the champions in even numbered indexes.

"""
def get_champion_slices(champions):
    return champions[2:], champions[:-2], champions[::2]