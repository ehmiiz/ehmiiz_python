
# if your age is 4 or below, price is 5
# if your age is under 18, the price is 10
# if your age is over 18, price is 15

age = 100

if age <= 4:
    price = 5
elif age <= 17:
    price = 10
else:
    price = 15

print(f'Your age is {age}, and therefore the cost is: ${price}')