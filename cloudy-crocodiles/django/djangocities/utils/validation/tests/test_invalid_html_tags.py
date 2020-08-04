import pytest

from djangocities.utils.validation.html import HtmlTag
from djangocities.utils.validation.html.parser import extract_active_tags
from djangocities.utils.validation.html.exceptions import (
    HtmlCommentError,
    InvalidHtmlTagError,
    NestedHtmlTagError,
)


class TestInvalidHtmlTags:
    def test_empty_tag(self, invalid_html_tag_empty):
        with pytest.raises(InvalidHtmlTagError):
            tag = HtmlTag("<>")

    def test_nested_tag(self):
        with pytest.raises(NestedHtmlTagError):
            _ = extract_active_tags("<<html>")

    def test_unclosed_tag(self):
        assert False
