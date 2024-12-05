# Poll users and display result
responses = {}

# Sets a flag for the while loop
polling_active = True

while polling_active:
    # Grab name
    name = input("What's your name? ")
    
    # Grab poll response
    response = input("What's your dream vacation? ")
    
    # sets the name variable as a `key` for the responses dict
    # sets the response as it's associated `value`
    responses[name] = response
    
    # More pollers?
    repeat = input("Poll next person? (Yes/No)")
    
    repeat.lower()    
    
    if repeat != 'yes':
        polling_active = False

print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f"{name.title()} would like to go to {response}")