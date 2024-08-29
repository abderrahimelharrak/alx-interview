#!/usr/bin/python3

"""Island perimeter finding function."""


def island_perimeter(grid):
    """Return the perimiter of an island.
    Grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    x = len(grid[0])
    y = len(grid)
    z = 0
    c = 0

    for i in range(y):
        for j in range(x):
            if grid[i][j] == 1:
                c += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    z += 1
    return c * 4 - z * 2
