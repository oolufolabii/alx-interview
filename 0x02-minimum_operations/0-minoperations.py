#!/usr/bin/python3
'''Coding challenge for computing minimum operations.
'''


def minOperations(n):
    '''Compute the fewest number of operations needed to result
    in exactly n-number of H characters.
    '''
    if not isinstance(n, int):
        return 0
    operation_count = 0
    clipboard = 0
    completed = 1

    while completed < n:
        if clipboard == 0:
            # init (the first copy all and paste)
            clipboard = completed
            completed += clipboard
            operation_count += 2

        elif n - completed > 0 and (n - completed) % completed == 0:
            # copy all and paste
            clipboard = completed
            completed += clipboard
            operation_count += 2

        elif clipboard > 0:
            # paste
            completed += clipboard
            operation_count += 1
    return operation_count
