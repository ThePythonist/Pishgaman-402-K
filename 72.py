pn = input("Enter phone number : ")

if pn[0] == "0":
    print(pn.replace("0", "+98", 1))
else:
    print(f"+98{pn}")
