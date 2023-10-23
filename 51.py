def mysort(items):
    # items.sort()
    # return items[::-1]

    items.sort(reverse=True)
    return items


print(mysort([10, 2, 1, 3, 4, 5]))
