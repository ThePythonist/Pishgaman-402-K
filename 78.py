lines = open("words.txt").readlines()
sublist = []
for i in lines:
    # if i[-4:] == "ing\n":
    if i[-4:-1] == "ing":
        sublist.append(i)

print(sublist)
