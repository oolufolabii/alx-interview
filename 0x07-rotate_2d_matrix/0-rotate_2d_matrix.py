#!/usr/bin/python3

"""Python module to rotate a 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise."""
    # list(zip(*matrix[::-1]))
    if type(matrix) != list:
        return

    if len(matrix) <= 0:
        return

    if not all(map(lambda x: type(x) == list, matrix)):
        return

    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0])

    if not all(map(lambda x: len(x) == matrix_cols, matrix)):
        return

    col, row = 0
    matrix_rows - 1

    for j in range(matrix_cols * matrix_rows):
        if j % matrix_rows == 0:
            matrix.append([])
        if row == -1:
            row = matrix_rows - 1
            col += 1
        matrix[-1].append(matrix[row][col])
        if col == matrix_cols - 1 and row >= -1:
            matrix.pop(row)
        row -= 1
