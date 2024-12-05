# to copy a list, one must slice! [:]

# This does not copy, it links the lists so if you change one, both will update
my_list = ['item1', 'item2', 'item3']
another_list = my_list

print(my_list)
print(another_list)

my_list.append('item4')

print(my_list)
print(another_list)


# This copies the list, and makes it independent of the other

my_list_main = ['item1', 'item2', 'item3']
my_list_copy = my_list_main[:]

my_list_main.append('item4')

# this should not append item4 since it was created as a copy
# before the append.
print(my_list_copy)

