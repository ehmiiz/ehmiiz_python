from pathlib import Path
import json


path = Path('user_information.json')

def get_user_name():
    """
    Ask for user data, write to json file.
    """
    name = input("Whats your name? ")
    age = input("Whats your age? ")
    computer_brand = input("What computer are you using? ")

    user_dictionary = {
        'user_name': name,
        'user_age': age,
        'user_comp': computer_brand,
    }

    # No user data, write to json
    content = json.dumps(user_dictionary)
    path.write_text(content)
    
    print("Stored json data.")

if path.exists():
    # User info is present, display
    content = path.read_text()
    user_data = json.loads(content)
    
    # Confirm the user
    current_user = input("Whats your name? ")
    
    if user_data['user_name'] == current_user:
        print(user_data)
    else:
        get_user_name()

    
else:
    get_user_name()