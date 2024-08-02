#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


solutions = []
"""The list of possible solutions to the N queens problem.
"""
n = 0
"""The size of the chessboard.
"""
pos = None
"""The list of possible positions on the chessboard.
"""


def input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global n
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def attacking(position0, position1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        position0 (list or tuple): The first queen's position.
        position1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    if (position0[0] == position1[0]) or (position0[1] == position1[1]):
        return True
    return abs(position0[0] - position1[0]) == abs(position0[1] - position1[1])


def grp_exists(grp):
    """Checks if a group exists in the list of solutions.

    Args:
        grp (list of integers): A group of possible positions.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for stin in solutions:
        x = 0
        for stin_pos in stin:
            for grp_pos in grp:
                if stin_pos[0] == grp_pos[0] and stin_pos[1] == grp_pos[1]:
                    x += 1
        if x == n:
            return True
    return False


def build_solution(row, group):
    """Builds a solution for the n queens problem.

    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions
    global n
    if row == n:
        tmp0 = group.copy()
        if not grp_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(n):
            a = (row * n) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(lambda x: attacking(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """Gets the solutions for the given chessboard size.
    """
    global pos, n
    pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))
    a = 0
    group = []
    build_solution(a, group)


n = input()
get_solutions()
for solution in solutions:
    print(solution)
