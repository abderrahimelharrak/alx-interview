#!/usr/bin/python3

""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    if (n < 2):
        return 0
    y, z = 0, 2
    while z <= n:
        if n % z == 0:
            y += z
            n = n / z
            z -= 1
       z += 1
    return y
