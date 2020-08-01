# Given an array arr of n unique non-negative integers, how can you most efficiently find a non-negative integer that is not in the array?

# Your solution should return such an integer or null if arr contains all possible integers.
# Analyze the runtime and space complexity of your solution.


import sys


def find_int(arr):
    """ Takes an array and returns a non-negative integer that is not in the original array. Returns null if all integers are in the array.

    Runtime: O(n)
    Spacetime: O(n)

    >>> find_int([0, 2, 1, 3, 4, 5, 11, 32, 42, 50, 100, 6])
    7

    >>> find_int([2, 4, 5, 1, 3])
    0

    >>> find_int([0, 2, 4, 5, 1, 3])
    6

    >>> find_int([0, 2, 4, 5, 1, 3, 6, 8])
    7

    >>> find_int([])
    0

    """

