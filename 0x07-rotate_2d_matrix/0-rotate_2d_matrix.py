#!/usr/bin/python3

"""2D matrix rotation.
"""


def rotate_2d_matrix(matrix):
    """Rotates a matrice by n 2D matrix in place.
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    li = len(matrix)
    cl = len(matrix[0])
    if not all(map(lambda i: len(i) == cl, matrix)):
        return
    C, l = 0, li - 1
    for x in range(cl * li):
        if x % li == 0:
            matrix.append([])
        if l == -1:
            l = li - 1
            C += 1
        matrix[-1].append(matrix[l][C])
        if C == cl - 1 and l >= -1:
            matrix.pop(l)
        l -= 1
