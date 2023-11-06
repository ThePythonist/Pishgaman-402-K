# text = input("Enter any text : ").split()
# print(max(text, key=len))
# -----------------------------------------------
text = input("Enter any text : ").split()
lengths = []

for i in text:
    lengths.append(len(i))

longest = max(lengths)

for i in text:
    if len(i) == longest:
        print(i)
