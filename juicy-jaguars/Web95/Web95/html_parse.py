"""Module used to parse HTML pages."""

from bs4 import BeautifulSoup
import re


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
        """Change BG color to white."""
        try:
            head = self.soup.head
            head.append(self.soup.new_tag('style', type='text/css'))
            head.style.append('body {background-color:#C0C0C0 !important;}')
        except KeyError:
            pass

    def parse_font(self):
        """Change fonts on site to Arial."""
        try:
            head = self.soup.head
            head.append(self.soup.new_tag('style', type='text/css'))
            head.style.append('body {font-family: Arial, \
sans-serif !important;}')
        except KeyError:
            pass

    def parse_derounder(self):
        """Make rounded borders square."""
        for element in self.soup.find_all(re.compile("*")):
            print(element)
            try:
                element["style"]["border-radius"] = "0"
            except KeyError:
                pass
