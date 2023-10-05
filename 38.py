shoppinglist = ["a4", "mouse", "pen", "a4", "keyboard", "pen", "battery", "flash drive"]
unique = []

for i in shoppinglist:
    if i not in unique:
        unique.append(i)

print(unique)
