"""
This module defines some custom exceptions, so we can catch more specific
exceptions.
"""


class HtmlValidationException(Exception):
    """
    Base catch-all class for Html validation errors
    """

    pass


class HtmlCommentError(HtmlValidationException):
    """
    Some comment error - either closing an unopened comment, not closing a
    comment, etc.
    """

    pass


class InvalidHtmlTagError(HtmlValidationException):
    """
    Exception for a tag that isn't properly formatted (opened, closed, etc.)
    """

    pass


class NestedHtmlTagError(HtmlValidationException):
    """
    Nested tag openings like "<<html"
    """

    pass


class UnsupportedHtmlTag(HtmlValidationException):
    """
    Tags that are not supported in this implementation, or by the HTML version,
    e.g. <div> in HTML 2.
    """

    pass
