def add_to_zero(nums):
    """ Given list of ints, return True if any two nums sum to 0.

    >>> add_to_zero([])
    False

    >>> add_to_zero([1])
    False

    >>> add_to_zero([1, 2, 3])
    False

    >>> add_to_zero([1, 2, 3, -2])
    True
    """


def is_anagram_of_palindrome(word):
    """ Is the word an anagram of a palindrome?
    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False
    """


def coins(num_coins):
    """ Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.

    >>> coins(1) == {1, 10}
    True

    >>> coins(2) == {2, 11, 20}
    True

    >>> coins(3) == {3, 12, 21, 30}
    True

    >>> coins(4) == {4, 13, 22, 31, 40}
    True

    >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
    True
    """


def has_balanced_brackets(phrase):
    """Does a given string have balanced pairs of brackets?

    Given a string as input, return True or False depending on whether the
    string contains balanced (), {}, [], and/or <>.
    """


def make_change(amount, denominations, index=0):
    """
    Write a function that, given:
    1. an amount of money
    2. a list of coin denominations
    computes the number of ways to make the amount of money
    with coins of the available denominations.

    >>> make_change(amount=4, denominations=[1,2,3])
    4
    [1,1,1,1]
    [1,1,2]
    [1,3]
    [2,2]

    >>> make_change(amount=20, denominations=[5, 10])
    3
    [5,5,5,5]
    [5,5,10]
    [10,10]
    """


def merge_ranges(lst):
    """
    In HiCal, a meeting is stored as tuples of integers (start_time, end_time).
    These integers represent the number of 30-minute blocks past 9:00am.
    For example:
    (2, 3) # meeting from 10:00 - 10:30 am
    (6, 9) # meeting from 12:00 - 1:30 pm
    Write a function merge_ranges() that takes a list of meeting time ranges
    and returns a list of condensed ranges.

    >>> merge_ranges([(3, 5), (4, 8), (10, 12), (9, 10), (0, 1)])
    [(0, 1), (3, 8), (9, 12)]

    >>> merge_ranges([(0, 3), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 8), (9, 12)]

    >>> merge_ranges([(0, 3), (3, 5)])
    [(0, 5)]

    >>> merge_ranges([(0, 3), (3, 5), (7, 8)])
    [(0, 5), (7, 8)]

    >>> merge_ranges([(1, 5), (2, 3)])
    [(1, 5)]
    """


def get_max_profit(prices):
    """ Finds the maximum profit for buying and selling stock within a day.

    >>> stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    >>> get_max_profit(stock_prices_yesterday)
    6

    >>> stock_prices_yesterday = [10, 3]
    >>> get_max_profit(stock_prices_yesterday)
    -7

    >>> stock_prices_yesterday = [1, 10, 7, 14, 2, 11]
    >>> get_max_profit(stock_prices_yesterday)
    13

    >>> stock_prices_yesterday = [11, 10, 9, 8, 2, 1]
    >>> get_max_profit(stock_prices_yesterday)
    -1

    >>> stock_prices_yesterday = [11, 9, 5, 2, 2, 0]
    >>> get_max_profit(stock_prices_yesterday)
    0

    >>> stock_prices_yesterday = [1, 1, 1, 1, 1, 1]
    >>> get_max_profit(stock_prices_yesterday)
    0
    """


def valid_parens_perms(num):
    pass


def zigzag(a):
    """
    >> > zigzag([9, 8, 8, 5, 3, 5, 3, 2, 8, 6])
    4

    >> > zigzag([2, 3, 1, 0, 2])
    3

    >> > zigzag([1, 2, 3, 2, 1])
    3

    >> > zigzag([2, 3, 1, 4, 2])
    5

    >> > zigzag([1, 2, 0, 3, 2, 1, 3, 2, 4, 0])
    6

    >> > zigzag([1, 2])
    2

    >> > zigzag([1, 2, 1])
    3

    >> > zigzag([1, 1])
    1

    """
