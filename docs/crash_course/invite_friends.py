# My implementation of the list exercise where
# a invite list is created and manipulated.
# The program should define a list, invite members
# Have a member bail out, replace that member
# Add 3 new members in the start, middle and end of the list
# Finally remove everyone but two members



# Define list
invite_list = ['freppe söderberg', 'ludde jeansson', 'björn strid', 'lex fridman', 'jeffrey snover', 'ricky gervais']

print("\nMy party invites:")
for member in invite_list:
    member_pretty = member.title()
    message = f"\tWelcome to my party: {member_pretty}!"
    print(message)


# Could not make it
not_available = 'ricky gervais'
invite_list.remove(not_available)

# New member
new_member = 'soffe propp'
new_member = new_member.title()

invite_list.append(new_member)


print(f"\nSadly {not_available.title()} could not make it. Instead we welcome {new_member}!")
for member in invite_list:
    member_pretty = member.title()
    message = f"\tWelcome to my party: {member_pretty}!"
    print(message)

# Found bigger table, add 3 more members
more_members = ['luttas pluttas'.title(), 'owe powwe'.title(), 'bapp bappsson'.title()]

# Start with adding to first place in the list
invite_list.insert(0, more_members[0])

# Calculate middle of invite_list and add member to middle of list
middle_value = len(invite_list) // 2
invite_list.insert(middle_value, more_members[1])

# Append a member to last element of list
invite_list.append(more_members[2])

print("\nGlad news! Bigger table was found. New guests will be invited!")
for member in invite_list:
    member_pretty = member.title()
    message = f"\tWelcome to my party: {member_pretty}!"
    print(message)

# Shrink the list
# Use .pop to exclude every member but the first two

print("\nBad news. Can only invite two people. You will get a notice if you can or can't come.")

for member in invite_list:
    uninvited = invite_list.pop()
    print(f"\tYou are uninvited: {uninvited.title()}. Sorry.")

for member in invite_list:
    uninvited = invite_list.pop()
    print(f"\tYou are uninvited: {uninvited.title()}. Sorry.")

for member in invite_list:
    print(f"\tYou are still welcome: {member.title()}")

amount_of_members = len(invite_list)
message = f"Thanks, all {amount_of_members} of you for the party."
print(message)