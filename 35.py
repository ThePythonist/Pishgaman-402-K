tedad = int(input("How many entries : "))
numbers = []

for i in range(tedad):
    x = float(input("Enter any number : "))
    numbers.append(x)

if len(numbers) == 0:
    pass
else:
    print(max(numbers))
