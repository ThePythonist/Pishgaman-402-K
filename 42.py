# numbers = []
#
# for i in range(4):
#     x = input("Entry : ")
#     try:
#         x = int(x)
#         numbers.append(x)
#     except ValueError:
#         pass
#
# print(numbers)

numbers = []

for i in range(4):
    x = input("Entry : ")
    if x.isdigit():
        numbers.append(int(x))

print(numbers)
