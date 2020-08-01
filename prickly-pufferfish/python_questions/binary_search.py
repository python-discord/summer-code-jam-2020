"""
In this challenge, you'll make binary search for the
classic children's guessing game
of "pick a number from 1 to 100".
"""


def binary_search(val):
    """ Using binary search, find val in range 1-100. Return # of guesses.
    >>> binary_search(50)
    1

    >>> binary_search(25)
    2

    >>> binary_search(75)
    2

    >>> binary_search(31) <= 7
    True

    >>> max([binary_search(i) for i in range(1, 101)])
    7
    """
