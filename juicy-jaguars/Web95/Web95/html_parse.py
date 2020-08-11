"""Module used to parse HTML pages."""

from bs4 import BeautifulSoup  # For parsing HTML code
import re  # For matching multiple/all variations of elements
import urllib.parse  # To parse urls to determine if they are relative or absolute


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
        for name in dir(self):  # Searches for functions with "parse_" at the start
            if name.startswith("parse_"):
                method = getattr(self, name)
                method()

    def parse_backgroundColor(self):
        """Change BG color to white."""
        try:
            head = self.soup.head  # Sets "head" to the <head> of the site you are trying to visit
            head.append(self.soup.new_tag('style', type='text/css'))  # Adds a style tag to the <head>
            head.style.append('body {background-color:#C0C0C0 !important;}')
            # ^ Sets the background color to a sad and dismal grey.
            # ^ It also marks it as important to overide original background color
        except KeyError:  # excepts KeyError & AttributeError as in some cases website do not have a <head> tag
            pass
        except AttributeError:
            pass

    def parse_font(self):
        """Change fonts on site to Arial.

        Fonts are changed to Arial accross any visited sites to make websites
        seem bland and uncreative
        """
        try:
            head = self.soup.head
            head.append(self.soup.new_tag('style', type='text/css'))
            head.style.append("""@font-face {{
                font-family: "Windows 95";
                src: url('{}/static/fonts/w-95-sans-serif.woff2') format('woff2'),
                url('{}/static/fonts/w-95-sans-serif.woff') format('woff');
                font-weight: normal;
                font-style: normal;
                }}""".format("http://" + self.request.META["HTTP_HOST"], "http://" + self.request.META["HTTP_HOST"]))
        except KeyError:  # excepts KeyError & AttributeError as in some cases website do not have a <head> tag
            pass
        except AttributeError:
            pass

        for element in self.soup.find_all(re.compile(".*")):  # Gets all the elements of the target website
            # ^ ".*" matches any charecter any number of times
            try:
                element["style"] = "font-family: 'Windows 95', Arial, sans-serif !important;" + element["style"]
                # ^ If a style attribute already exists it append a font-family to it, else \/
            except KeyError:
                # If an element does not have a style attribute a KeyError will be raised.
                # We catch this and create a style attribute
                element["style"] = "font-family: 'Windows 95', Arial, sans-serif !important;"

    def parse_derounder(self):
        """Make rounded borders square."""
        for element in self.soup.find_all(re.compile(".*")):
            try:
                element["style"] = "border-radius: 0px !important; " + element["style"]
            except KeyError:
                element["style"] = "border-radius: 0px !important; "

    def parse_links(self):
        """Parse all links in document."""
        link_attrs = ["src", "href", "action", "data", "background", "formaction", "icon"]

        for element in self.soup.find_all(re.compile(".*")):  # \/
            for name, val in element.attrs.items():  # Returns each atribute of every element on the target webpage
                if name in link_attrs:  # Checks if the atribute should be a link or not
                    if ":" not in val:
                        # ^ If no ":" is found in the link atribute, it is asummed that the link is relative
                        # ^ "http://example.com/image.png" vs "../Images/image.png"
                        element[name] = "/page/" + urllib.parse.quote(self.link_parent(self.basedir) + val)
                        # ^ Converts relative links to absolute links

                elif name == "srcset":
                    values = list(map(lambda x: x.split(" "), val.split(",")))
                    values = list(map(self.remove_blanks, values))
                    new_values = []
                    print(values)
                    for x in values:
                        if ":" not in x[0]:
                            x[0] = urllib.parse.quote(self.link_parent(self.basedir) + x[0])
                        try:
                            new_values.append([x[0], " ".join(x[1:])])
                        except IndexError:
                            new_values.append([x[0], ""])

                    print((",".join(list(map(lambda x: "/" + (" ".join(x)), new_values)))))

                    element[name] = (",".join(list(map(lambda x: "/" + (" ".join(x)), new_values))))

    def remove_blanks(self, x):
        """Remove blank strings from x."""
        y = []
        for item in x:
            if item != " " * len(item):
                y.append(item)
        return y

    def link_parent(self, link):
        """Get the parent of a link."""
        link_parts = link.split("/")

        if len(link_parts) == 3:
            return "/".join(link_parts)
        else:
            return "/".join(link_parts[:-1])

    def parse_color(self):
        """Make document greyscale."""
        try:
            head = self.soup.head
            head.append(self.soup.new_tag('style', type='text/css'))
            head.style.append('html {filter: grayscale(80%) !important;}')
        except KeyError:
            pass
        except AttributeError:
            pass
