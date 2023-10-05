x = 12
divisors = []

for i in range(1, x + 1):
    if x % i == 0:
        divisors.append(i)

print(divisors)