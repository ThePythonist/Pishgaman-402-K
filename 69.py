def f1():
    text = input("Enter any text : ").split()
    print(max(text, key=len))


# def f2():
#     text = input("Enter any text : ").split()
#     lengths = []
#
#     for i in text:
#         lengths.append(len(i))
#
#     longest = max(lengths)
#
#     for i in text:
#         if len(i) == longest:
#             print(i)

def f3():
    text = input("Enter any text : ").split()
    text.sort(key=len)
    print(text[-1])


f3()
