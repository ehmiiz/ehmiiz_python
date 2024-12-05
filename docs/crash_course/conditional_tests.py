# true conditions

first_boy = 'lucas'
if first_boy == 'lucas':
    print(f'My first boy was {first_boy.title()}!')

second_boy = 'oliver'
if (second_boy == 'oliver') and (first_boy != 'oliver'):
    print(f'My second boy was {second_boy.title()}!')

if (first_boy == 'lucas') and (second_boy == 'oliver'):
    print(f'{first_boy.title()} and {second_boy.title()} are my boys!')

cars = ['Tesla', 'Subaru']
model = ['Model Y', 'Outback']

if cars[0] == 'Tesla':
    print(f'My first EV was a {cars[0]}.')

if (cars[0] == 'Tesla') and (model[0] == 'Model Y'):
    print(f'My first EV was a {cars[0]} {model[0]}.')

if (cars[1] != 'Tesla') or (model[1] == 'Outback'):
    print(f'My first AWD was a {cars[1]} {model[1]}, and not a {cars[0]}.')


if len(cars) < 3:
    print('I have less than 3 cars!')

if len(cars) > 1:
    print('I have more than 1 car!')

if len(cars) == 2:
    print('I have 2 cars.')

boys = first_boy[:], second_boy[:]

if len(cars) == 2 and (len(boys) == 2):
    print('I have 2 cars and 2 boys.')


# False conditions

if len(boys) == 3:
    print('I have 3 boys!')

if len(cars) > 2:
    print('I have more than 2 cars!')

if first_boy == 'Oliver':
    print('Oliver was my first boy!')

if second_boy == 'Lucas':
    print('Lucas was my second boy!')

if cars[0] == 'Subaru':
    print('My newest car is a Subaru.')

if 'Volvo' in cars:
    print('I have a Volvo!')

if 'Tesla' in cars and 'Subaru' in cars:
    print('I have a Tesla and a Subaru!')

if ('Tesla' in cars) or ('Volvo' in cars):
    print('I have either a Tesla or a Volvo!')

if (first_boy.lower == 'lucas'):
    print(f'My first boy was {first_boy.title()}')