# Some data
message = ['My name is Emil', 'Hello World', 'Starcraft Rocks']
sent_message = []

# Define
def send_message(message, sent_message):
    """Prints a list of messages and moves it to a new list."""
    for mes in message[:]:
        current_message = message.pop()
        print(mes)
        sent_message.append(current_message)

# Calls the function
# Remove the slice to actually move items from target -> destination
send_message(message[:], sent_message)


# Test results
print(f"Target list: {message}")
print(f"Destination list: {sent_message}")