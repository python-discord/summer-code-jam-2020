# Allows using HtmlTag as a type hint in the HtmlTag class
from __future__ import annotations

from math import inf
from numbers import Number
from typing import Callable, Optional
import logging

from djangocities.utils.validation.html.exceptions import (
    InvalidHtmlTagError,
    UnsupportedHtmlTag,
)


class HtmlTag:
    """
    An instance of an HTML tag, such as <a>, </a>, or <br>.
    """

    def __init__(
        self,
        _tag_name: str,
        validator: Optional[Callable[[HtmlTag], bool]] = None,
        min_version: Number = 0,
        max_version: Number = inf,
    ) -> None:
        """
        Constructor.

        Arguments:
            - _tag_name: the tag name with or without brackets, e.g. "a" or "<a>"
            - validator: a custom validation function, if the default is not enough.
            - min_version: version the tag was introduced
            - max_version: version the tag was deprecated

        Note that some double tags (e.g. <p>) are valid even without their closing counterpart.

        Also, see the validate method to see which arguments the custom validator should take. As
        of writing, it takes an HTML version, but this is subject to change.
        """
        tag_name = _tag_name.lstrip("<").rstrip(">")
        if not len(tag_name):
            logging.debug("tag cannot be empty")
            raise InvalidHtmlTagError("tag cannot be empty")
        self.name = tag_name
        self.validator = validator
        self.min_version = min_version
        self.max_version = max_version

    def _validate(self, version):
        """
        Default validator. Checks that users do not try to use a "style" attribute,
        and that the tag is allowed in the current
        """
        pass

    def validate(self, version):
        if self.validator is not None:
            return self.validator(version)
        return self._validate(version)

    @staticmethod
    def get_tag_name(tag_content) -> str:
        return tag_content.split(" ", 1)[0]

    @staticmethod
    def unsupported_tag(_):
        logging.debug("this tag is not allowed")
        raise UnsupportedHtmlTag("this tag is not allowed")


HTML_TAGS = {
    "!doctype": HtmlTag(_tag_name="!doctype", validator=HtmlTag.unsupported_tag),
    "a": HtmlTag(_tag_name="a"),
    "address": HtmlTag(_tag_name="address"),
    "area": HtmlTag(_tag_name="area", min_version=2),
    "b": HtmlTag(_tag_name="b", min_version=2),
    "blockquote": HtmlTag(_tag_name="blockquote", min_version=2),
    "body": HtmlTag(_tag_name="body", min_version=2),
    "br": HtmlTag(_tag_name="br", min_version=2),
    "caption": HtmlTag(_tag_name="caption", min_version=2),
    "cite": HtmlTag(_tag_name="cite", min_version=2),
    "code": HtmlTag(_tag_name="code", min_version=2),
    "col": HtmlTag(_tag_name="col", min_version=2),
    "colgroup": HtmlTag(_tag_name="colgroup", min_version=2),
    "dd": HtmlTag(_tag_name="dd"),
    "dfn": HtmlTag(_tag_name="dfn", min_version=2),
    "dir": HtmlTag(_tag_name="dir", max_version=3.99),
    "dl": HtmlTag(_tag_name="dl"),
    "dt": HtmlTag(_tag_name="dt"),
    "em": HtmlTag(_tag_name="em", min_version=2),
    "form": HtmlTag(_tag_name="form", min_version=2),
    "head": HtmlTag(_tag_name="head", min_version=2),
    "h1": HtmlTag(_tag_name="h1"),
    "h2": HtmlTag(_tag_name="h2"),
    "h3": HtmlTag(_tag_name="h3"),
    "h4": HtmlTag(_tag_name="h4"),
    "h5": HtmlTag(_tag_name="h5"),
    "h6": HtmlTag(_tag_name="h6"),
    "hr": HtmlTag(_tag_name="hr", min_version=2),
    "html": HtmlTag(_tag_name="html", min_version=2),
    "i": HtmlTag(_tag_name="i", min_version=2),
    "img": HtmlTag(_tag_name="img", min_version=2),
    "input": HtmlTag(_tag_name="input", min_version=2),
    "isindex": HtmlTag(_tag_name="isindex", max_version=3.99),
    "kbd": HtmlTag(_tag_name="kbd", min_version=2),
    "li": HtmlTag(_tag_name="li"),
    "listing": HtmlTag(_tag_name="listing", max_version=1.99),
    "map": HtmlTag(_tag_name="map", min_version=2),
    "menu": HtmlTag(_tag_name="menu"),
    "meta": HtmlTag(_tag_name="meta", min_version=2),
    "ol": HtmlTag(_tag_name="ol", min_version=2),
    "option": HtmlTag(_tag_name="option", min_version=2),
    "p": HtmlTag(_tag_name="p"),
    "plaintext": HtmlTag(_tag_name="plaintext", max_version=1.99),
    "pre": HtmlTag(_tag_name="pre", min_version=2),
    "samp": HtmlTag(_tag_name="samp", min_version=2),
    "select": HtmlTag(_tag_name="select", min_version=2),
    "strike": HtmlTag(_tag_name="strike", min_version=2, max_version=3.99),
    "strong": HtmlTag(_tag_name="strong", min_version=2),
    "table": HtmlTag(_tag_name="table", min_version=2),
    "tbody": HtmlTag(_tag_name="tbody", min_version=2),
    "td": HtmlTag(_tag_name="td", min_version=2),
    "textarea": HtmlTag(_tag_name="textarea", min_version=2),
    "tfoot": HtmlTag(_tag_name="tfoot", min_version=2),
    "th": HtmlTag(_tag_name="th", min_version=2),
    "thead": HtmlTag(_tag_name="thead", min_version=2),
    "title": HtmlTag(_tag_name="title"),
    "tr": HtmlTag(_tag_name="tr", min_version=2),
    "tt": HtmlTag(_tag_name="tt", min_version=2),
    "u": HtmlTag(_tag_name="u"),
    "ul": HtmlTag(_tag_name="ul", min_version=2),
    "var": HtmlTag(_tag_name="var", min_version=2),
    "xmp": HtmlTag(_tag_name="xmp", min_version=2),
}
