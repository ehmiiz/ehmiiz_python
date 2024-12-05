# Person
person = {
    'first_name': 'emil',
    'last_name': 'larsson',
    'age': 31,
    'city': 'boxholm',
}

for per in person.values():
    print(per)

# Favorit Number

favorit_numbers = {
    'emil': '1337',
    'baba': '1',
    'lutt': '3',
}

for name, number in favorit_numbers.items():
    print(f'{name.title()}s favorit number is {number}')

