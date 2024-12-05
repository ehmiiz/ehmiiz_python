# Counting to 20
for value in range(1, 21):
    print(value)

# print 1 mil
one_million = range(1, 1_000_001)
for value in one_million:
    print(value)

# min value
print(min(one_million))

# max value
print(max(one_million))

odd_numbers = list(range(1, 21, 2))
for odd_number in odd_numbers:
    print(odd_number)

# multiples of 3
three = list(range(1, 31))
for value in three:
    print(value * 3)

# Cube numbers 1 - 10
cubes = []
for value in range(1, 10):
    cubes.append(value ** 3)
print(cubes)

# List comprehensions of cubes
list_cubes = [value ** 3 for value in range(1, 10)]
print(list_cubes)

