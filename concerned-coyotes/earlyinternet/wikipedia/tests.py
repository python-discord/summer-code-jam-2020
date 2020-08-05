import unittest
from .utils import WikipediaFeaturedArticleParser, create_url_with_query_parameters


class TestUtils(unittest.TestCase):
    def test_create_url_with_query_parameters(self):
        base_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "dog": "bark",
            "chicken": "egg",
            "cow": "muh"
        }
        expected_result = f"{base_url}?dog=bark&chicken=egg&cow=muh"

        self.assertEqual(create_url_with_query_parameters(base_url, params),
                         expected_result)

    def test_wikipedia_article_parser(self):
        # Some shortened wikipedia summary like it is given
        # when the api is called
        summary = (
            '<div class="mw-parser-output"><p><i><b><a>Banksia sessilis</a></b></i> '
            'is a large shrub or small tree in the <a>family</a> <a>Proteaceae</a>. '
            'First collected and described by <a>Robert Brown</a> in the early 19th '
            'century, the species grows widely throughout <a >southwest</a> '
            '<a>Western Australia</a>. It has prickly dark green leaves and '
            'dome-shaped cream-yellow <a>flowerheads</a>. '
            '(<b><a href="/wiki/Banksia_sessilis" title="Banksia sessilis">'
            'Full&#160;article...</a></b>) </p><div> Recently featured: '
            '<div class="hlist hlist-separated inline"><ul><li><i>'
            '<a>Trials of Mana</a></i></li><li><a>Brownsea Island Scout '
            'camp</a></li><li><a>Rodrigues rail</a></li></ul></div></div></div>'
        )

        html_parser = WikipediaFeaturedArticleParser()
        html_parser.feed(summary)

        expected_title = "Banksia sessilis"
        expected_url = "https://en.wikipedia.org/wiki/Banksia_sessilis"
        expected_content = (
            "Banksia sessilis is a large shrub or small tree in the family "
            "Proteaceae. First collected and described by Robert Brown "
            "in the early 19th century, the species grows widely throughout "
            "southwest Western Australia. It has prickly dark green leaves "
            "and dome-shaped cream-yellow flowerheads."
        )

        self.assertEqual(html_parser.title, expected_title)
        self.assertEqual(html_parser.article_url, expected_url)
        self.assertEqual(html_parser.content, expected_content)
