#!/usr/bin/python3
"""Python Module for Grid Perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""

    visited = set()

    def depth_search(i, j):
        """Counts the perimeter using depth search"""
        if i >= len(grid) or j >= len(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0:
            return 1

        if (i, j) in visited:
            return 0

        visited.add((i, j))

        perimeter = depth_search(i, j+1)
        perimeter += depth_search(i+1, j)
        perimeter += depth_search(i, j-1)
        perimeter += depth_search(i-1, j)

        return perimeter

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return depth_search(i, j)
