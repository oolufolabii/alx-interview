#!/usr/bin/python3
"""Python Module for Grid Perimeter"""
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """returns the perimeter of the island described in grid"""

    def search(matrix):
        """Counts the perimeter using depth search"""
        count = 0
        for row in matrix:
            row = [0] + row + [0]
            for i in range(1, len(row)):
                count += row[i] != row[i-1]
        return count

    tgrid = [[] for _ in range(len(grid[0]))]
    for row in grid:
        for i, item in enumerate(row):
            tgrid[i].append(item)

    return search(grid) + search(tgrid)
