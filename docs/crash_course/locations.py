locations = ['Spain', 'America', 'Norway']

# Original list
print(locations)

# Sort and print
print(sorted(locations))

# Prove the original list has not changed
print(locations)

# Sort reverse and print
print(sorted(locations, reverse=True))

# Prove the original list has not changed
print(locations)

# reverse the order
locations.reverse()
print(locations)

# reverse the order again
locations.reverse()
print(locations)

# sort permanently and print
locations.sort()
print(locations)

# sort reverse permanently and print
locations.sort(reverse=True)
print(locations)

