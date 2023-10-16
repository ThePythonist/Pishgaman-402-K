x = input("Entry : ")
numbers = []

while x != "exit":
    try:
        x = float(x)
        if x == int(x):
            numbers.append(int(x))
        else:
            numbers.append(x)
    except ValueError:
        pass

    x = input("Entry : ")
else:
    print("Pressed Exit")

print(numbers)
print(max(numbers))
