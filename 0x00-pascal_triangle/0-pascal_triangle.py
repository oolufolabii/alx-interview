#!/usr/bin/python3

def pascal_triangle(n):
    result = [[1]]

    for i in range(n - 1):
        temp_result = [0] + result[-1] + [0]
        new_row = []
        for j in range(len(result[-1]) + 1):
            new_row.append(temp_result[j] + temp_result[j+1])
        result.append(new_row)

    return (result)
