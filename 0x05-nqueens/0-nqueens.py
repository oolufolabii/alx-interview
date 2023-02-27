#!/usr/bin/python3

"""Python module on N queens puzzle"""

import sys

possible_solutions = []
# n = 0
possible_position = None


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

def attacking_queen(position_1, position_2):
	"""Checker for attacking position of the Queen.
	Returns True if the queens are in an attacking
	position else False."""
	if ([position_1][0] == position_2[0]) or ([position_1][1] == position_2[1]):
		return True
	return abs([position_1][0] - position_2[0]) == abs([position_1][1] - position_2[1])

# print(user_input())
