"""
This module defines some custom exceptions, so we can catch more specific
exceptions.
"""


class HtmlCommentError(Exception):
    """
    Some comment error - either closing an unopened comment, not closing a
    comment, etc.
    """

    pass


class InvalidHtmlTagError(Exception):
    """
    Exception for a tag that isn't valid.
    """

    pass


class NestedHtmlTagError(Exception):
    """
    Nested tag openings like "<<html"
    """

    pass
