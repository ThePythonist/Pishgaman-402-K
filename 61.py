def func(x, y):
    if y == 1:  # Shart payan
        return x
    else:  # Shart edame
        return x + func(x, y - 1)


func(4, 3)