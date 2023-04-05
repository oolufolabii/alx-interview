#!/usr/bin/python3
"""Python module for a prime numbers game"""


def prime_checker(num):
    """Return True if number is prime otherwise false"""
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True


def prime_calculator(x, prime_num):
    """Calculate the prime numbers"""
    max_prime = prime_num[-1]
    if x > max_prime:
        for i in range(max_prime + 1, x + 1):
            if prime_checker(i):
                prime_num.append(i)
            else:
                prime_num.append(0)


def isWinner(x, nums):
    """
    Gets the winner of a prime game with 'x' amount of rounds.
    """

    wins_dict = {"Maria": 0, "Ben": 0}

    primes = [0, 0, 2]

    prime_calculator(max(nums), primes)

    for round in range(x):
        summation = sum((i != 0 and i <= nums[round])
                        for i in primes[:nums[round] + 1])

        if (summation % 2):
            round_winner = "Maria"
        else:
            round_winner = "Ben"

        if round_winner:
            wins_dict[round_winner] += 1

    if wins_dict["Maria"] > wins_dict["Ben"]:
        return "Maria"
    elif wins_dict["Ben"] > wins_dict["Maria"]:
        return "Ben"

    return None
