def check(word):
    if len(word) == len(set(word)):
        return False
    else:
        return True
    # smt = ""
    # for i in word:
    #     if i not in smt:
    #         smt += i
    #
    # print(smt)


print(check("ali"))
