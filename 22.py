import math

print("Ax^2 + Bx + C")

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

delta = (b ** 2) - (4 * (a * c))
radicaldelta = math.sqrt(delta)

if delta == 0:
    x = (-b) / (2 * a)
    print(x)
elif delta < 0:
    print("X doesnt exists")
else:
    x1 = ((-b) + radicaldelta) / (2 * a)
    x2 = ((-b) - radicaldelta) / (2 * a)
    print(x1, x2)
