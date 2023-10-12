def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


x = int(input("Enter any numer : "))

if x > 0:
    print(factorial(5))
elif x == 0:
    print(1)
else:
    print("Factorial of negative number doesnt exists")
