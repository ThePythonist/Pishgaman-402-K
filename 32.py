# numbers = []
#
# for i in range(5):
#     x = int(input("Enter any number (between 1-10) :"))
#     if 0 < x < 10:
#         numbers.append(x)
#
# print(numbers)

# -----------------------------------------

# numbers = []
# count = 0
# while count != 5:
#     x = int(input("Enter any number (between 1-10) :"))
#     if 0 < x < 10:
#         numbers.append(x)
#         count += 1
#
# print(numbers)
# -----------------------------------------

numbers = []
while len(numbers) != 5:
    x = int(input("Enter any number (between 1-10) :"))
    if 0 < x < 10:
        numbers.append(x)

print(numbers)
