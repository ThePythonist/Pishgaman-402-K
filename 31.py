items = [10, 2.5, "Apple", "Sony", 5, 6, 15.7, "Microsoft"]
strings = []

for item in items:
    if type(item) == str:
        strings.append(item)

print(strings)
