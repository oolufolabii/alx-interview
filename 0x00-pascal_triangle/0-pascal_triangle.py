#!/usr/bin/python3
"""A module for working with Pascal's triangle.

    """


def pascal_triangle(n):
    """Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.

    Args:
        n (int): number of triangles/levels

    Returns:
        array: array of pascal triangle
    """
    result = []
    if type(n) is not int or n <= 0:
        return result
    result = [[1]]
    for i in range(n):
        temp_result = [0] + result[-1] + [0]
        new_row = []
        for j in range(len(result[-1]) + 1):
            new_row.append(temp_result[j] + temp_result[j+1])
        result.append(new_row)

    return (result)
