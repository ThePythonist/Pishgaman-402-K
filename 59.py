def func(x, y):
    if y == 1:  # Shart payan
        return x + 1
    else:  # Shart edame
        return 1 + func(x, y - 1)


print(func(2, 4))
