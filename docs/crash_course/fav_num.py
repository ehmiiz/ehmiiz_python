# peoples fav numbers

sof_fav_numb = [23, 7]

people = {
    'emil': [5, 1],
    'sofie': [6, 7]
}

for name, numbers in people.items():
    print(f"{name.title()}s favorite numbers are:")
    for num in numbers:
        print(f"{num}")