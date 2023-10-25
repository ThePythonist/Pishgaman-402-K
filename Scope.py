balance = 0


def show_balance():
    print(balance)


def transaction(value):
    global balance
    balance += value


transaction(-300)
print(balance)
