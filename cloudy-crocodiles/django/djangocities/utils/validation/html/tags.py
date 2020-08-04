# Allows using HtmlTag as a type hint in the HtmlTag class
from __future__ import annotations

from typing import Callable, Optional

from djangocities.utils.validation.html.exceptions import InvalidHtmlTagError


class HtmlTag:
    """
    An instance of an HTML tag, such as <a>, </a>, or <br>.
    """

    def __init__(
        self,
        _tag_content: str,
        valid_single: bool = True,
        valid_double: bool = True,
        validator: Optional[Callable[[HtmlTag], bool]] = None,
    ) -> None:
        """
        Constructor.

        Arguments:
            - _tag_content: the tag name without brackets, e.g. 'a href="index.html"'
            - valid_single: whether the tag can be used without a matching closing tag, e.g. <br>
            - valid_double: whether the tag can be used with a matching closing tag, e.g. <p> and </p>
            - validator: a custom validation function, if the default is not enough.

        Note that some double tags (e.g. <p>) are valid even without their closing counterpart.
        """
        tag_content = _tag_content.lstrip("<").rstrip(">")
        if not len(tag_content):
            raise InvalidHtmlTagError("tag cannot be empty")
        self.tag_name = self.get_tag_name(tag_content)

    def _validate(self, text):
        """
        Default validator.
        """
        pass

    def validate(self, text):
        if self.validator is not None:
            return self.validator(text)
        return self._validate(text)

    @staticmethod
    def get_tag_name(tag_content) -> str:
        return tag_content.split(" ", 1)[0]
