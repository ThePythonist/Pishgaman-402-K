# number = input("Enter any number : ")
# try:
#     number = int(number)
#     print("It is a number")
# except ValueError:
#     print("It is not a number")

# ------------------------------------------------

# try:
#     print(x)
# except NameError:
#     print("X not found")
#
# print("Edame")

# ------------------------------------------------

# try:
#     # x = int("ali")
#     # print(x)
#     print([1,2,3][4])
# except (NameError, ValueError, IndexError):
#     print("Something went wrong")

# ------------------------------------------------

# number = input("Enter any number : ")
# try:
#     number = int(number)
#     print("It is a number")
# except:
#     print("It is not a number")

# ------------------------------------------------

try:
    x = int("ali")
    print("It is a number")
except Exception as khata:
    print(khata)

print("edameye barname")
