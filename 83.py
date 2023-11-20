lines = open("words.txt").readlines()
revlines = []
for i in lines:
    revlines.append(i[::-1])

# print(revlines)
output = "".join(revlines)
open("reversedwords.txt", "w").write(output)
