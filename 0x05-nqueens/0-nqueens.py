#!/usr/bin/python3

"""Python module on N queens puzzle"""

import sys

pos_sol = []
j = 0
pos= None


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


def create_solution(row, group):
    """Creating a solution for the n queen problem"""

    global pos_sol
    global j

    if row == j:
        tmp0 = group.copy()
        if not solution_check(tmp0):
            pos_sol.append(tmp0)
    else:
        for col in range(j):
            a = (row * j) + col
            matches = zip(list([pos[a]]) * len(group), group)
            used_positions = map(
                lambda x: attacking_queen(x[0], x[1]), matches)
            group.append(pos[a].copy())
            if not any(used_positions):
                create_solution(row + 1, group)
            group.pop(len(group) - 1)



def get_solutions():
    """Gets the solutions for the given chessboard size.
    """
    global pos, j
    pos = list(map(lambda x: [x // j, x % j], range(j ** 2)))
    n = 0
    group = []
    create_solution(n, group)
    
a = user_input()
get_solutions()
for solution in pos_sol:
    print(solution)