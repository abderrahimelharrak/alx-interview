#!/usr/bin/python3
"""
First project 0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Function def pascal_triangle(n): that returns a list of lists
    """
    y = []
    if n > 0:
        for x in range(1, n + 1):
            niveau = []
            c = 1
            for z in range(1, x + 1):
                niveau.append(c)
                c = c * (x - z) // z
            y.append(niveau)
    return y
