# def func(x):
#     divs = [i for i in range(1, x + 1) if x % i == 0]
#     return divs
#
# m = map(func, [12, 21, 9])
# for i in m:
#     print(i)

m = map(lambda x: [i for i in range(1, x + 1) if x % i == 0], [12, 21, 9])
for i in m:
    print(i)
