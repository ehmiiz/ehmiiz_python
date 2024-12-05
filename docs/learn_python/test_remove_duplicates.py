def remove_duplicates(lst):
    return set(lst)

lst = [1, "ludde", 2, 3, 4, 5, 6, 7, "ludde", 8, 9, 10, 1, 2, 3, 4, 5, "emil", "emil"]
print(remove_duplicates(lst))