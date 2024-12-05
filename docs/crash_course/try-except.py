# Ask for numerical, input text, catch the error


while True:
    print("type 'q' to quit.")
    number_one = input("Number 1: ")
    if number_one.lower() == "q":
        break
    number_two = input("Number 2: ")

    if number_two == "Q":
        break

    try:
        added_numbers = int(number_one) + int(number_two)
        print(added_numbers)
    except ValueError:
        print("You must provide numbers.")