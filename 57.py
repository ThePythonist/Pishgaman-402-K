def check_status(x):
    x = int(x)

    if x % 2 == 0:
        return "even"
    else:
        return "odd"


def check_type(x):
    if x.isdigit():
        print(check_status(x))
    else:
        print("Entry is not a number")


check_type(input("Entry : "))
