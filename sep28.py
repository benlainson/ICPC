# Given a price over n days
# Can buy and sell on a later day
# Determine max profit
# Only one transaction


def max_profit():
    inp = [5, 2, 9, 1, 6, 8]
    cp = 0
    mp = 9999999
    profit = 0
    best = 0
    for i in inp:
        cp = i
        if i < mp:
            mp = cp
        profit = cp - mp
        if profit > best:
            best = profit


    print(f"Best price: {best}")


max_profit()
