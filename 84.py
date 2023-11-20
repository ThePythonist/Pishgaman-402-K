lines = open("words.txt").read().split("\n")
numbers = []

for i in lines:
    if i.isdigit():
        numbers.append(i)

print(numbers)
