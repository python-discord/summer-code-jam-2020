from django.shortcuts import redirect
from django.urls import reverse
from GoogleNews import GoogleNews

from .models import NewsHistory

import ast


class TerminalCommand():
    """Container for terminal all terminal commands"""

    def __init__(self, command_string: str, request):
        self.specified_method = command_string.split()[0]
        self.params = command_string[command_string.find(" ") + 1:]
        self.request = request

    def run(self, **kwargs):
        try:
            method_to_call = getattr(self, self.specified_method)
            response = method_to_call(self.params, **kwargs)
        except AttributeError as e:
            response = {'response': f"{self.specified_method}: command not found"}
        return response

    def logout(self, params=None, **kwargs):
        redirect = reverse('logout')
        message = f"Logged out {self.request.user.username}"
        return {'response': message, 'redirect': redirect}

    def signup(self, params=None, **kwargs):
        if self.request.user.is_authenticated:
            message = "Log out to create a new account"
            return {'response': message}
        else:
            redirect = reverse('signup')
            message = "enter details to signup"
            return {'response': message, 'redirect': redirect}

    @staticmethod
    def message(params: str = None, **kwargs):
        help_text = "message: use this to send messages<br><br>"\
            "Usage: message username [args] [message text]<br>"\
            "options:<br>"\
            "--help: get help (this screen)<br>"\
            "--last: view the last message sent to the user<br>"

        if params.split()[0] == '--help':
            message = help_text
        elif params.count(' ') == 0:
            message = "Message text not provided <br>"\
                "Usage: message username message text"
        else:
            user = params.split()[0]
            message = f"Message delivered to {user}."
        return {'response': message}

    @staticmethod
    def news(topic: str, start_date: str = None, end_date: str = None, **kwargs):
        page_num = int(kwargs.get('Page', '0'))
        article_num = int(kwargs.get('Article', '0'))
        if page_num == 0 and article_num == 0:
            try:
                NewsHistory.objects.latest('search_time').delete()
            except Exception as e:
                print("No news history for this user", repr(e))
            googlenews = GoogleNews()
            googlenews.search(topic)
            googlenews.getpage(1)
            articles = googlenews.result()
            articles = [article for article in articles if len(article['title']) > 10]
            db_entry = NewsHistory(user_id=1, search_topic=topic, last_fetched_count=0, news_articles=str(articles))
            articles = articles[0:3]
            db_entry.save()
        else:
            news_list = NewsHistory.objects.latest('search_time')
            news_items = ast.literal_eval(news_list.news_articles)
            if page_num != 0:
                article_start_num = page_num * 3
                articles = news_items[article_start_num:article_start_num+3]
            elif article_num != 0:
                article = news_items[article_num - 1]
                article_link = '<a href="{}" target="_blank">Read full article</a>'.format(article['link'])
                article = "<br>" + "<br>".join([article['title'], article['desc'], article_link])
                return {'response': article}

        article_text = []
        for i, article in enumerate(articles):
            serial_number = str(i + 1 + page_num * 3)
            article_summary = (serial_number, f"{article['date']}, {article['media']}", article['title'])
            article_text.append(article_summary)
        all_articles = "<br>".join([", ".join(i) for i in article_text])
        return {'response': all_articles, 'followup': True}
