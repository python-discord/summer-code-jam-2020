from django.core.exceptions import ValidationError

from djangocities.utils.validation.html.parser import extract_active_tags
from djangocities.utils.validation.html.exceptions import (
    HtmlCommentError,
    InvalidHtmlTagError,
    NestedHtmlTagError,
)


def _validate_html(html, tag_validator=None):
    """
    Validates HTML, and, if tag_validator is not None, also validates its
    contained tags.
    """
    try:
        tags = extract_active_tags(html)
        if tag_validator is not None:
            tag_validator(tags)
    except (HtmlCommentError, InvalidHtmlTagError, NestedHtmlTagError) as e:
        raise (ValidationError(e))
