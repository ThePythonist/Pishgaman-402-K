def func(number):
    number = str(number)
    # n = 0
    # for digit in number:
    #     n += int(digit)
    #
    # print(n)

    digits = [int(i) for i in number]
    print(sum(digits))


func(1024)
