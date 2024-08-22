#!/usr/bin/python3

"""Change comes from within.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    minmum_coins = [float('inf')] * (total + 1)
    minimum_coins[0] = 0

    for x in coins:
        for y in range(x, total + 1):
            minimum_coins[y] = min(minimum_coins[y], minimum_coins[i - x] + 1)

    return minimum_coins[total] if minimum_coins[total] != float('inf') else -1
