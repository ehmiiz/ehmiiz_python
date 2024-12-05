def double_string(string):
    # create an empty list to store the strings in 
    list = []

    for s in string:
        # double each element and add it to the list
        list.append(s + s)

    # join on an empty string and return the result
    return "".join(list)