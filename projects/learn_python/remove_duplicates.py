"""
    To "Select -Unique" in python, you can use a set
    The following code takes a list of spells
    Creates a set from it, and an empty list
    Then iterates over the set, appending each element to the list
    Finally, it returns the list
"""
def remove_duplicates(spells):
    return_set = set(spells)
    return_list = []
    for r in return_set:
        return_list.append(r)
    return return_list

"""
    The following just removes duplicates from a list of strings
"""
def remove_duplicates(lst):
    return set(lst)