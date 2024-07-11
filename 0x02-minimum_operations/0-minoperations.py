#!/usr/bin/python3
"""
Function that calculates the min operations to copy and paste letters
"""


def minOperations(n):
    numberOpe = 0
    minimumOpe = 2
    while n > 1:
        while n % minimumOpe == 0:
            numberOpe += minimumOpe
            n /= minimumOpe
        minimumOpe += 1
    return numberOpe
