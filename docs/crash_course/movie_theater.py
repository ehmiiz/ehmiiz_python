# if under 3, its free
# between 3 and 12, its $10
# if above 12, it's $15

print('Welcome to the movies.')
active = True

while(active):
    message = input('Enter your age to get a price: ')
    if message:
        message = int(message)
        if message < 3:
            price = 'free'
        elif message < 12:
            price = 10
        else:
            price = 15

        if price == 'free':
            print(f"It's {price}!")
        else:
            print(f"That would be ${price}.")
    else:
        # active = False
        break