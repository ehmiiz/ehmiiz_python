# Arbitrary parameter value
def make_sandwich (*toppings):
    """Prints a sandwich construction based on given toppings."""
    print('Making a sandwich with:')
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('cheese')
make_sandwich('cheese', 'ham')
make_sandwich('cheese', 'ham', 'sallad')