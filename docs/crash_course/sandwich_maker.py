# This program moves items from a list to another list using
# a while loop.
sandwich_orders = ['ost', 'pastrami', 'skinka', 'pastrami', 'pastrami']

finished_sandwiches = []

# A while loop can be used to remove duplicates from a list
print('Sorry but we are out of pastrami.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print('Removing pastrami order..')

while sandwich_orders:
    
    # Pops the last sandwich
    current_sandwich = sandwich_orders.pop()
    
    # Simulate a make function
    print(f"Making: {current_sandwich.title()}...")
    
    # Adds completed sandwich to list
    finished_sandwiches.append(current_sandwich)

print("We have made:")
for f in finished_sandwiches:
    print(f.title())