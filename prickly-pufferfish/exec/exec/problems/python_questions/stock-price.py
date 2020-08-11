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
