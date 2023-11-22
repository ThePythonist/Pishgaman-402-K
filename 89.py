from random import *


def generate1(length):
    password = []

    for i in range(length):
        digit = str(randint(0, 9))
        password.append(digit)

    password = "".join(password)
    return password


def generate2(length):
    password = sample(range(1, 10), length)
    password = [str(i) for i in password]
    return "".join(password)


# print(generate1(4))
print(generate2(6))
