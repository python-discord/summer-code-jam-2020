import pytest

from djangocities.utils.validation.html.tags import HTML_TAGS
from djangocities.utils.validation.html.exceptions import UnsupportedHtmlTag


class TestHtmlTagClass:
    def test_doctype_is_banned(self):
        doctype = HTML_TAGS["!doctype"]
        with pytest.raises(UnsupportedHtmlTag):
            doctype.validate(1)
