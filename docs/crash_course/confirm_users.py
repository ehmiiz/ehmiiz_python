unconfirmed_users = ['luppo', 'frello', 'ehmmo']

confirmed_users = []

while unconfirmed_users:
    
    current_user = unconfirmed_users.pop()
    
    print(f"Confirmed: {current_user.title()}")
    confirmed_users.append(current_user)

print("We have confirmed:")
for c in confirmed_users:
    print(c.title())