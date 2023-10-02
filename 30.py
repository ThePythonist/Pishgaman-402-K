items = [10, 2.5, "Apple", "Sony", 5, 6, 15.7, "Microsoft"]
numbers = []

for item in items:
    if type(item) == int or type(item) == float:
        numbers.append(item)

print(numbers)
