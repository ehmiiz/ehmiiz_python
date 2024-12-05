from pathlib import Path

# Ask user for name
user_name = input("Whats your name? ")


# Write to file
path = Path("guests.txt")
path.write_text(user_name)