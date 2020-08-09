import datetime
import typing
import unicodedata
from html.parser import HTMLParser
from time import mktime

import feedparser


class WikipediaFeaturedArticleParser(HTMLParser):
    def __init__(self) -> "WikipediaFeaturedArticleParser":
        super().__init__()
        self._title = ""
        self._content = ""
        self._article_url = ""

        self._tag = ""
        self._current_tag_attributes = {}

    @property
    def content(self) -> str:
        # Parsed content needs to be stripped of the "Recently featured..."
        # part
        #
        # Parsed content looks like ([...] means that a part was obmitted
        # because it would be too long for this comment section):
        #
        # John Leak (c. 1892 – 1972) was an Australian recipient of the
        # Victoria Cross, the highest award for gallantry in battle that
        # could be awarded at that time to a member of the Australian
        # armed forces.[...] and died in 1972. (Full article...) [...]

        try:
            content_end_index = self._content.index("(Full article...)")
        except ValueError:
            content_end_index = self._content.index(
                "(This article is part of a featured topic")

        return self._content[:content_end_index].strip()

    @property
    def title(self) -> str:
        return self._title

    @property
    def article_url(self) -> str:
        return f"https://en.wikipedia.org{self._article_url}"

    def handle_starttag(
        self,
        tag: str,
        attrs: typing.List[typing.Tuple[str, str]]
    ) -> None:
        """Handles the start of a tag. Always stores the attributes in a
        variable to be used to get the full url and title for the full
        article page."""
        self._tag = tag
        self._current_tag_attributes = {key: value for key, value in attrs}

    def handle_data(self, data: str) -> None:
        """Handles the inner html data for all tags."""
        # data sometimes has strings encoded in Latin1 (ISO 8859-1)
        # as well as some endline characters, which are removed.
        normalized_string = unicodedata.normalize("NFKC",
                                                  data.replace("\n", ""))
        self._content += normalized_string

        # The string is surrounded by a html link to the full article
        # which data is stored in _current_tag_attributes
        if normalized_string in ["Full article...", "This article"] and self._tag == "a":
            self._title = self._current_tag_attributes["title"]
            self._article_url = self._current_tag_attributes["href"]


def get_wikipedia_featured_articles() -> typing.List[dict]:
    """Returns a list of all featured wikipedia articles for
    the last 10 days."""

    # Create the URL for the RSS feed
    base_url = "https://en.wikipedia.org/w/api.php"
    parameters = {
        "action": "featuredfeed",
        "feed": "featured",
        "feedformat": "rss"
    }
    url = create_url_with_query_parameters(base_url, parameters)

    # Get the feed and parse it
    feed = feedparser.parse(url)

    # Go through all entries and parse their articles
    articles: typing.List[dict] = []
    for entry in feed["entries"]:
        # Each entry has a summary which consists of html elements,
        # which we have to remove as we want to display plain text
        html_parser = WikipediaFeaturedArticleParser()
        html_parser.feed(entry["summary"])

        # Get date of article
        date = datetime.datetime.fromtimestamp(
            mktime(entry["published_parsed"]))

        articles.append({
            "title": html_parser.title,
            "date": date,
            "url": html_parser.article_url,
            "content": html_parser.content,
        })

    return articles


def create_url_with_query_parameters(base_url: str, params: dict) -> str:
    """Creates a url for the given base address with given parameters
    as a query string."""

    parameter_string = "&".join(f"{key}={value}"
                                for key, value in params.items())
    url = f"{base_url}?{parameter_string}"

    return url
