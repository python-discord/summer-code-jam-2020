import logging

from djangocities.utils.validation.html.parser import extract_active_tags
from djangocities.utils.validation.html.exceptions import (
    HtmlCommentError,
    InvalidHtmlTagError,
    NestedHtmlTagError,
    UnsupportedHtmlTag,
)
from djangocities.utils.validation.html.tags import HTML_TAGS


def tag_is_allowed(_tag, version):
    """
    Checks if the tag is allowed to be used in the current HTML version, and by
    the site.
    """
    try:
        # Extract tag content
        _tag = _tag.lower().lstrip("<").lstrip("/").rstrip(">").split(" ")[0]
        tag = HTML_TAGS[_tag]
    except KeyError:
        logging.debug(f"tag {_tag} is either invalid, or unsupported on this site")
        raise UnsupportedHtmlTag(
            f"tag {_tag} is either invalid, or unsupported on this site"
        )


def validate_html(html, version):
    """
    Validates HTML, and, if tag_validator is not None, also validates its
    contained tags.

    Might raise:
        HtmlCommentError
        InvalidHtmlTagError
        NestedHtmlTagError
        UnsupportedHtmlTag
    Use try/except in models clean method.
    """
    tags = extract_active_tags(html)
    for tag in tags:
        tag_is_allowed(tag, version)
