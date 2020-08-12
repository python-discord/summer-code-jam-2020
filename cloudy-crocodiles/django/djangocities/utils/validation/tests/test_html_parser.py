import pytest

from djangocities.utils.validation.html.parser import extract_active_tags


class TestHtmlParser:
    def test_extract_tags(self, html_file, html_file_tags):
        assert extract_active_tags(html_file) == html_file_tags
