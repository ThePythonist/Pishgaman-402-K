numbers = []

for i in range(4):
    x = input("Entry : ")
    try:
        x = float(x)
        # if str(x)[-2:] == ".0":
        if x == int(x):
            numbers.append(int(x))
        else:
            numbers.append(x)
    except ValueError:
        pass

print(numbers)
