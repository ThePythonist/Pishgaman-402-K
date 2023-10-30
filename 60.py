def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


x = input("Enter any number : ")

try:
    x = int(x)
    if x > 0:
        print(factorial(x))
    elif x == 0:
        print("Factorial of 0 is 1")
    else:
        print("Factorial of negative number doesnt exist")
except ValueError:
    print("Entry must be integer")
