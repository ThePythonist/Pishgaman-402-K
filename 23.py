# x = int(input("Enter any number : "))
# numbers = [124, 136, 958]
#
# if x % 2 == 0 and 100 <= x <= 999:
#     numbers.append(x)
#
# print(numbers)
# -------------------------------------------------------------
x = int(input("Enter any number : "))
numbers = [124, 136, 958]

if x % 2 == 0 and len(str(x)) == 3:
    numbers.append(x)

print(numbers)
