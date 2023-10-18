def checknumber(x):
    if type(x) in [int, float]:
        # print("Okay continue")
        return "Number"
    else:
        # print("Not okay")
        return "Not Number"


# print(checknumber(50))

#
# if checknumber(43) == "Number":
#     print("Yes")
# else:
#     print("No")

# -------------------------------------------

# def checknumber(x):
#     if x % 2 == 0:
#         print("Even")
#         # return "Even"
#     else:
#         print("Odd")
#         # return "Odd"


# checknumber(14)
# print(checknumber(14))

# if checknumber(8) == "Even":
#     print("Pasokh zoj ast")

# numbers = [11, 4, 2, 3, 5, 12, 16]
# for i in numbers:
#     checknumber(i)


# print(checknumber(12))


def gozinesh(x):
    if x % 2 == 0:
        print(x)


numbers = [11, 4, 2, 3, 5, 12, 16]
for i in numbers:
    gozinesh(i)
