rivers = {
    'Dalaälven': 'Sweden',
    'Themsen': 'England',
    'Seine': 'France',
}

# Items gets both key and value
for river, c in rivers.items():
    print(f"The river {river} runs through {c}.")


# Key is the name of the property
for river in rivers.keys():
    print(river)

# Value is the property value
for c in rivers.values():
    print(c)