"""
Collection of HTML parsing functions.
"""

import logging

from djangocities.utils.validation.html.exceptions import (
    HtmlCommentError,
    InvalidHtmlTagError,
    NestedHtmlTagError,
)


def find_tag_positions(html: str) -> list:
    """
    Finds the position of HTML opening and closing tag characters ("<", ">").

    Args:
        - html: the HTML string to parse
    Returns: list of positions. Note that it includes all tags, even those in
    comments, and they should be ignored. (The extract_active_tags function
    takes care of that.)

    >>> find_tag_positions("<html>")
    [0, 5]
    """
    return [i for i, c in enumerate(html) if c in ("<", ">")]


def extract_active_tags(html: str) -> list:
    """
    Extracts a list of tags that are not inside comments.

    Raises InvalidHtmlTagError if html is invalid
    """
    # Variables to test that the HTML is properly formatted
    in_tag = False
    in_comment = False

    tag_start = None

    tag_positions = find_tag_positions(html)
    active_tags = []

    for p in tag_positions:
        if html[p] == "<":
            if in_comment:
                continue
            if html[p : p + 4] == "<!--":
                if in_comment:
                    logging.debug("nested comments are not allowed")
                    raise HtmlCommentError("nested comments are not allowed")
                in_comment = True
                continue
            if in_tag:
                logging.debug("nested tag found")
                raise NestedHtmlTagError("nested tag found")
            in_tag = True
            tag_start = p
        elif html[p] == ">":
            if p > 1 and html[p - 2 : p + 1] == "-->":
                if not in_comment:
                    logging.debug("cannot close comment when no comment opened")
                    raise HtmlCommentError(
                        "cannot close comment when no comment opened"
                    )
                in_comment = False
                continue
            if in_comment:
                continue
            if not in_tag:
                logging.debug("cannot close tag that was not opened")
                raise InvalidHtmlTagError("cannot close tag that was not opened")
            in_tag = False
            active_tags.append(html[tag_start : p + 1])

    # Should not be in an unclosed tag or comment after looping through the
    # entire list
    if in_tag:
        logging.debug("file cannot end with unclosed tag")
        raise InvalidHtmlTagError("file cannot end with unclosed tag")
    if in_comment:
        logging.debug("file cannot end with an open comment tag")
        raise HtmlCommentError("file cannot end with an open comment tag")

    return active_tags
