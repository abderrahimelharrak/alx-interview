#!/usr/bin/python3

"""Maria and Ben are playing a game"""


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    m = [1 for x in range(sorted(nums)[-1] + 1)]
    m[0], m[1] = 0, 0
    for i in range(2, len(m)):
        rmmultiples(m, i)

    for i in nums:
        if sum(m[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rmmultiples(y, x):
    """removes multiple
    of primes
    """
    for i in range(2, len(y)):
        try:
            y[i * x] = 0
        except (ValueError, IndexError):
            break
