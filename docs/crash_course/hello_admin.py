users = ['elarsson', 'admin', 'balrog', 'corpuser', 'batman']

if users:
    for user in users:
        if user == 'admin':
            print('Hello Admin! Welcome.')
        else:
            print(f'Hello {user}.')

current_users = ['elarsson', 'balrog', 'batman']
new_users = ['elarssoN', 'frezzy', 'superman']

for user in new_users:
    if user.lower() in current_users:
        print(f'{user} is a current user. Pick a new name.')
    else:
        print(f'Username: {user} is free!')


# Ordinal Numbers 1-9


numbers = range(1,10)

for n in numbers:
    if n == 1:
        suffix = 'st'
    elif n == 2:
        suffix = 'nd'
    elif n == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(f'{n}{suffix.lower()}')