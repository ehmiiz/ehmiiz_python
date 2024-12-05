from pathlib import Path
import json

# Get the path of json file
path = Path('username.json')


def set_users_favorite_number():
    """
    Gets the users favorite number and
    stores it in a json file.
    """
    
    # Ask the user
    favorite_number = input("Whats your favorite number? ")

    # Convert output to a json object
    content = json.dumps(favorite_number)

    # Take the path, write the converted content to it.
    path.write_text(content)


def get_users_favorite_number():
    """
    Reads a specific json file, shows the user
    it's content.
    """
    if path.exists():
        content = path.read_text()
        print(f"I know your favorite number: {content}")
    else:
        set_users_favorite_number()

get_users_favorite_number()