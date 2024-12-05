"""
    A set can be returned to a list using the list function
    The following function takes two lists, converts them to sets to
    remove duplicates and then returns the difference between the two sets as a list
"""
def find_missing_ids(first_ids, second_ids):
    first_set = set(first_ids)
    second_set = set(second_ids)

    return list(first_set - second_set)
