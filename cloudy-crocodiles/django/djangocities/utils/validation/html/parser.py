"""
Collection of HTML parsing functions.
"""

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

    tag_positions = find_tag_positions(html)
    comment_tag_positions = []

    for p in tag_positions:
        if html[p] == "<":
            if in_comment:
                continue
            if html[p : p + 4] == "<!--":
                if in_comment:
                    raise HtmlCommentError("nested comments are not allowed")
                in_comment = True
                comment_tag_positions.append(p)
                continue
            if in_tag:
                raise NestedHtmlTagError("nested tag found)")
            in_tag = True
        elif html[p] == ">":
            if p > 1 and html[p - 2 : p + 1] == "-->":
                if not in_comment:
                    raise HtmlCommentError(
                        "cannot close comment when no comment opened"
                    )
                in_comment = False
                comment_tag_positions.append(p)
            in_tag = False

    # Should not be in an unclosed tag or comment after looping through the
    # entire list
    if in_tag:
        raise InvalidHtmlTagError("file cannot end with unclosed tag")
    if in_comment:
        raise HtmlCommentError("file cannot end with an open comment tag")

    return [tag for tag in tag_positions if tag not in comment_tag_positions]


sample_html = """
<!-- this is a comment -->
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
"""

print(extract_active_tags(sample_html))
