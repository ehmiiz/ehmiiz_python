how_many = input('How many people needs a table? ')

how_many = int(how_many)

if (how_many >= 8):
    print("Since you are more than eight, i'm afraid you'll have to wait.")
else:
    print(f"Oh, only {how_many}? We'll fix that right away.")