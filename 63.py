def summarize(number):
    if len(str(number)) == 1:
        return number
    else:
        digits = [int(i) for i in str(number)]
        number = sum(digits)
        return summarize(number)


print(summarize(56561))
