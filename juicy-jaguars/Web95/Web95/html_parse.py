"""Module used to parse HTML pages."""

from bs4 import BeautifulSoup
import re


class HtmlParser:
    """Class used to parse HTML."""

    def __init__(self, html, basedir, request):
        """Store HTML, setup Soup."""
        self.html = html
        self.soup = BeautifulSoup(html, "html.parser")
        self.basedir = basedir
        self.request = request

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
        except AttributeError:
            pass

    def parse_font(self):
        """Change fonts on site to Arial."""
        try:
            head = self.soup.head
            head.append(self.soup.new_tag('style', type='text/css'))

            head.style.append("""@font-face {{
    font-family: "Windows 95";
    src: url('{}/static/fonts/w-95-sans-serif.woff2') format('woff2'),
         url('{}/static/fonts/w-95-sans-serif.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}}""".format("http://"+self.request.META["HTTP_HOST"],
             "http://"+self.request.META["HTTP_HOST"]))
        except KeyError:
            pass
        except AttributeError:
            pass

        for element in self.soup.find_all(re.compile(".*")):
            try:
                element["style"] = "font-family: 'Windows 95', Arial, \
    sans-serif !important;" + element["style"]
            except KeyError:
                element["style"] = "font-family: 'Windows 95', Arial, \
    sans-serif !important;"

    def parse_derounder(self):
        """Make rounded borders square."""
        for element in self.soup.find_all(re.compile(".*")):
            try:
                element["style"] = "border-radius: 0px !important; " + \
                                   element["style"]
            except KeyError:
                element["style"] = "border-radius: 0px !important; "

    def parse_links(self):
        """Parse all links in document."""
        link_attrs = ["src", "href", "action", "data", "background",
                      "formaction", "icon"]

        for element in self.soup.find_all(re.compile(".*")):
            for name, val in element.attrs.items():
                if name in link_attrs:
                    if val.startswith("/"):
                        element[name] = self.basedir + val

    def parse_color(self):
        """Make document greyscale."""
        head = self.soup.head
        head.append(self.soup.new_tag('style', type='text/css'))
        head.style.append('html {filter: grayscale(100%) !important;}')
