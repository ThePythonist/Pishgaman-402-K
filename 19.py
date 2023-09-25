age = int(input("Enter your age : "))
names = ["aria", "mamad"]

if age >= 18:
    name = input("Enter your name : ")
    names.append(name)
else:
    print("You're not allowed")
    print("🖕")
    # print("👍")


print(names)
