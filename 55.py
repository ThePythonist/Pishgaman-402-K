# def is_prime(x):
#     divisors = [i for i in range(1, x + 1) if x % i == 0]
#     print("Prime") if len(divisors) == 2 else print("Composite")
#
#
# x = int(input("Enter any number : "))
# is_prime(x)


def is_prime(x):
    divisors = [i for i in range(1, x + 1) if x % i == 0]
    return "Prime" if len(divisors) == 2 else "Composite"


x = int(input("Enter any number : "))
print(is_prime(x))
