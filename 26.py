# entry = input("Entry : ")

# while entry != "exit":
#     print(entry)
#     entry = input("Entry : ")
# else:
#     print("Pressed Exit")


flag = 1

while flag:
    entry = input("Entry : ")
    if entry == "exit":
        flag = 0

    print(entry)
