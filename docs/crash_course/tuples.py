# immutable lists are called tuple, they can't be modified
# however they can be over-written (with assignment)

tuples_foods = ('Sandwich', 'Stake', 'Sallad', 'Hotdog', 'Hamburger')

for t in tuples_foods:
    print(t)

# This errors out
# tuples_foods[0] = 'Soda'

# This does the same but does not error out
tuples_foods = ('Soda', 'Stake', 'Sallad', 'Hotdog', 'Hamburger')
for t in tuples_foods:
    print(t)
