def is_binary(number):
    characters = {"0", "1"}
    for i in number:
        if i not in characters:  # Ragham gheir binary ast
            return False

    return True


numbers = []

for i in range(4):  # Khandan adad az vorodi
    x = input("Enter any number : ")
    numbers.append(x)

for i in numbers:
    print(is_binary(i))
