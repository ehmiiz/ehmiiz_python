
# gets element 0-1
print('gets element 0-1')
players = ['emil', 'sofie', 'owe', 'lutt']
print(players[0:2])


# gets last two elements
print('gets last two elements')
players = ['emil', 'sofie', 'owe', 'lutt']
print(players[-2:])

# gets everything but the first
print('gets everything but the first')
players = ['emil', 'sofie', 'owe', 'lutt']
print(players[1:])

# loop thru a slice
print('loops thru a slice')
for player in players[1:3]:
    print(player)