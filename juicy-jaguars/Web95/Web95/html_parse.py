"""Module used to parse HTML pages."""

from bs4 import BeautifulSoup


class HtmlParser:
    """Class used to parse HTML."""

    def __init__(self, html):
        """Store HTML, setup Soup."""
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")

    def parse(self):
        """Run all parsing functions."""
        for name in dir(self):
            if name.startswith("parse_"):
                method = getattr(self, name)
                method()
