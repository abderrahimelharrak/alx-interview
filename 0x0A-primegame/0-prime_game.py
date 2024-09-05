#!/usr/bin/python3

"""Module defining isWinner function."""


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    maria = 0
    ben = 0

    for num in nums:
        roundSet = list(range(1, num + 1))
        primeSet = primes_in_range(1, num)

        if not primeSet:
            ben += 1
            continue

        MariaTurns = True

        while(True):
            if not primeSet:
                if MariaTurns:
                    ben += 1
                else:
                    maria += 1
                break

            smallestPrime = primeSet.pop(0)
            roundSet.remove(smallestPrime)

            roundSet = [x for x in roundSet if x % smallestPrime != 0]

            MariaTurns = not MariaTurns

    if maria > ben:
        return "Winner: Maria"

    if maria < ben:
        return "Winner: Ben"

    return None


def its_prime(y):
    """Returns True if n is prime, else False."""
    if y < 2:
        return False
    for i in range(2, int(y ** 0.5) + 1):
        if y % i == 0:
            return False
    return True


def primes_in_range(start, end):
    """Returns a list of prime numbers between start and end (inclusive)."""
    primes = [m for m in range(start, end+1) if its_prime(m)]
    return primes
