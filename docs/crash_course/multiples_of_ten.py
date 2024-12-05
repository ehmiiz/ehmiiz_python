pick_number = input("Pick a number, and I'll see if it's multiple of 10.\n")

pick_number = int(pick_number)

# since '%'/modulus operator selects the "leftovers" from a division, anything
# that is true is not a multiple of ten. Meanwhile anything that is 0 (in the else)
# clause, is a multiple of ten.

if pick_number % 10:
    print("nope.")
else:
    print(f"{pick_number} is multiple of ten!")