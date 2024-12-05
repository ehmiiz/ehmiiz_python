pizzas = ['Kebab', 'Vesuvio', 'Azteka', 'America', 'Venedig', 'Margareta']

print(f"First 3 items in the list: {pizzas[0:3]}")

print(f"First 3 from the middle of the list: {pizzas[2:5]}")

print(f"Last 3 from in the list: {pizzas[-3:]}")

for pizza in pizzas:
    full_pizza_name = f"{pizza}pizza"
    print(f"I love {full_pizza_name}")

print("\nI love pizza!")

# Make a new list, add a new pizza to the old list without
# editing the new list
friend_pizza = pizzas[:]
pizzas.append('New Pizza')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friends favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)