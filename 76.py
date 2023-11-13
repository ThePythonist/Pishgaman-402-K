def f1():
    lines = open("words.txt", "r").readlines()
    longest = max(lines, key=len)
    print(longest)
    print(len(longest))


def f2():
    lines = open("words.txt", "r").readlines()
    lines.sort(key=len)
    longest = lines[-1]
    print(longest)
    print(len(longest))


def f3():
    lines = open("words.txt", "r").readlines()
    longest = len(max(lines, key=len))

    for i in lines:
        if len(i) == longest:
            print(i)


f3()
