from pathlib import Path
import json

def main():
    # Read data
    kata_data = read_kata_json()
    
    # Display selection of katas
    display_supported_kata_selection(kata_data)
    
    # Display full kata
    display_kata(kata_data)

def read_kata_json():
    """Reads and returns kata.json"""
    script_dir = Path(__file__).parent
    json_kata_path = script_dir / "kata.json"

    return json.loads(json_kata_path.read_text())

def display_supported_kata_selection(kata_data):
    """Lists all supported katas."""
    for index, kata in enumerate(kata_data, start=1):
        print(f"{index}. {kata}")

def get_user_selection(num_options):
    """Gets validated user selection"""
    while True:
        try: # catch invalid input
            user_input = input(f'Enter between 1 and {num_options}: ').strip()
            if not user_input.isdigit():
                raise ValueError("Input invalid.")
            userselection = int(user_input)
            if 1 <= userselection <= num_options:
                return userselection
            else:
                print(f"Not in range of 1 and {num_options}")
        except ValueError as e:
            print(e)
            

def display_kata(katadata):
    """Displays the kata"""
    keys = list(katadata.keys())
    userselection = get_user_selection(len(keys))
    if 1 <= userselection <= len(keys): # catch out of range input numbers
        for value in katadata[keys[userselection - 1]].values():
            print(value)
    
if __name__ == "__main__":
    main()