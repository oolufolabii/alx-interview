#!/usr/bin/python3

"""Python module on N queens puzzle"""

import sys

pos_sol = []
j = 0
pos_sol = None


def user_input():
    """Get and validate the users input or argument"""
    global j
    j = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        j = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if j < 4:
        print("N must be at least 4")
        sys.exit(1)
    return j
# print(user_input())


def attacking_queen(pos_1, pos_2):
    """Checker for attacking position of the Queen.
    Args: Both arguments are either a list or tuple.
    Returns True if the queens are in an attacking
    position else False."""
    if (pos_1[0] == pos_2[0]) or (pos_1[1] == pos_2[1]):
        return True
    return abs(pos_1[0] - pos_2[0]) == abs(pos_1[1] - pos_2[1])
# print(attacking_queen((2,4), (2,4)))


def solution_check(options):
    """Checking if the option exist in a list of possible
    solutions.
    Returns True if it exists, otherwise False."""
    global pos_sol

    for soln in pos_sol:
        i = 0
        for sol_pos in soln:
            for opt_pos in options:
                if sol_pos[0] == opt_pos[0] and sol_pos[1] == opt_pos[1]:
                    i += 1

            if i == j:
                return True
    return False
