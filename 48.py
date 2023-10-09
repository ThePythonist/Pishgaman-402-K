# word = "engineer"
# slices = {}
# index = 0
#
# for i in word:
#     slices.setdefault(index,i)
#     index += 1
#
# print(slices)

# ------------------------------------------------

# word = "engineer"
# slices = {}
#
# for i in range(len(word)):
#     slices.setdefault(i,word[i])
#
# print(slices)

# ------------------------------------------------

word = "engineer"
slices = dict(zip(range(len(word)), word))
print(slices)
