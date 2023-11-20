lines = open("words.txt").read().split("\n")
numbers = []

for i in lines:
    if not i.isdigit():
        for j in i:
            if j.isdigit():
                numbers.append(i)
                break

print(numbers)
