message = ""
while message != 'quit':
    print("Add the topping 'quit' to exit the program.")
    topping = input("What topping would you like on your pizza?\n")
    
    if topping == 'quit':
        break
    
    print(f"Sure, I'll add {topping}")