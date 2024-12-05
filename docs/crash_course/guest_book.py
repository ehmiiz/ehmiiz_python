from pathlib import Path

active = True

path = Path("guest_book.txt")
file_data = ""

while active:
    
    user_input = ""
    user_input = input("Type Q to exit. Whats your name? ")
    
    if user_input == "q":
        active = False
    else:
        file_data += str(user_input + "\n")

path.write_text(file_data)