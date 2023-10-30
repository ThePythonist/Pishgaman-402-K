def func(x, y):
    # for i in range(y):
    #     x += 1
    #
    # print(x)

    counter = 0

    while counter < y:
        x += 1
        counter += 1

    print(x)


func(2, 4)
