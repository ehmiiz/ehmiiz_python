def display_message():
    """Print's a simple message."""
    print("I'm learning Python!")
display_message()

# the parameter `Title` now has a default parameter value.
def favorite_book(title='Shell of an idea'):
    """Dynamically prints what my favorite book is based on a parameter."""
    print(f"My favorite book is: {title.title()}")

# All three examples below generates the same output

# Positional Argument, here we only have 1 parameter, so the position is 0
favorite_book("Shell of an idea")

# Keyword Argument
favorite_book(title="Shell of an idea")

# Using the default value
favorite_book()