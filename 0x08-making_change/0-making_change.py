#!/usr/bin/python3
""" Change comes from within"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    x = 0
    coins = sorted(coins)[::-1]
    for c in coins:
        while c <= total:
            total -= c
            x += 1
        if (total == 0):
            return x
    return -1
