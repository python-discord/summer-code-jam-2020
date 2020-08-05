"""
This modules contains fixtures to test the HTML parser.
"""

import pytest


@pytest.fixture
def html_file():
    return """<!DOCTYPE html>
<!-- this is a comment -->
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
  """


@pytest.fixture
def html_file_tags():
    return [
        "<!DOCTYPE html>",
        "<html>",
        "<head>",
        "<title>",
        "</title>",
        "</head>",
        "<body>",
        "<h1>",
        "</h1>",
        "<p>",
        "</p>",
        "</body>",
        "</html>",
    ]


@pytest.fixture
def html_2_file():
    return """<!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
  <!-- Here, have some comment
  <b>With a mismatched tag
  <em  And another tag that isn't even closed OR formatted properly
  -->
  <head>
    <title>Hello World</title>
  </head>
  <body>
    <p>Welcome to my site
    <p>Be sure to sign my guestbook
  </body>
</html>
    """


@pytest.fixture
def invalid_html_tag_empty():
    return "<>"
