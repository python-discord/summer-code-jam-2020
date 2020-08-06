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

    for j, n in enumerate(nums):
        for i, n2 in enumerate(nums):
            if n + n2 == 0 and i != j:
                return True
    return False
