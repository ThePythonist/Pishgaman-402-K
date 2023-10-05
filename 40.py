x = 12
divisors = []

for i in range(1, x + 1):
    if x % i == 0:
        divisors.append(i)

print(divisors)

# if divisors == [1, x]:
if len(divisors) == 2:
    print("Prime")
else:
    print("Composite")
