x = 10
divs = [i for i in range(1, x) if x % i == 0]
print((lambda x: True if sum(divs) == x else False)(x))
