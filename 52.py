def is_perfect(x):
    divisors = []

    for i in range(1, x):
        if x % i == 0:
            divisors.append(i)

    print(divisors)

    if sum(divisors) == x:
        return True
    else:
        return False


print(is_perfect(28))
