odds = []
# number = 1

# while number <= 20:
#     if number % 2 != 0:
#         odds.append(number)
#     number += 1

# while number <= 20:
#     if number % 2 == 1:
#         odds.append(number)
#     number += 1

# while number <= 20:
#     odds.append(number)
#     number += 2
#
# print(odds)


for i in range(1,20):
    if i % 2 == 1:
        odds.append(i)

print(odds)