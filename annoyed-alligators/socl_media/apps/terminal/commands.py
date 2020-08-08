from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from typing import Callable
from .models import NewsHistory
from socl_media.apps.chat.models import Message
from GoogleNews import GoogleNews
import ast


class Command():
    """
    This class is the blueprint for all
    terminal commands."""

    commands_list = []

    def __init__(self, name: str, help_text: str, action: Callable):
        self.name = name
        self.help_text = help_text
        self.action = action
        self.__class__.commands_list.append(self)


def add_linebreaks(msg: str):
    """This function is used to add the <br> tag to the response message."""
    return "<br>" + msg


def logout(request, params: str, **kwargs):
    if request.user.is_authenticated:
        redirect = reverse('logout')
        message = f"Logged out {request.user.username}"
        messages.success(request, message)
        return {'response': add_linebreaks(message), 'redirect': redirect}
    else:
        return {'response': add_linebreaks("No user Logged in")}


logout = Command(name='logout', help_text="""Logs out current user.<br>
Usage: logout<br>""",
                 action=logout)


def signup(request, params: str, **kwargs):
    if request.user.is_authenticated:
        message = "Log out to create a new account"
        return {'response': add_linebreaks(message)}
    else:
        redirect = reverse('signup')
        message = "Enter details to Sign Up"
        messages.success(request, message)
        return {'response': add_linebreaks(message), 'redirect': redirect}


signup = Command(name='signup', help_text="""Register a new user.<br>
Make sure you are logged out to register a new user.<br>
Usage: signup<br>""",
                 action=signup)


def message(request, params: str, **kwargs):
    print(params)
    if not params:
        message = "Incorrect usage. See: message --help"
    else:
        receiver_username = params.split()[0]

        if receiver_username == request.user.username:
            message = "You can't send a message to yourself."
        else:
            try:
                receiver_obj = User.objects.get(username=receiver_username)
                if len(params.split()) > 1:
                    message_body = params[params.find(" ") + 1:]
                    message = "No message provided. See: message --help"
                    Message.objects.create(body=message_body, sender=request.user, recipient=receiver_obj)
                    message = f"Message sent to {receiver_username}"
                else:
                    message = "No message provided. See: message --help"

            except User.DoesNotExist:
                message = f"User '{receiver_username}' does not exist. Enter a valid username."

    return {'response': add_linebreaks(message)}


message = Command(name='message', help_text="""Send a personal message to any user.<br>
Usage: message [username] [message body]""",
                  action=message)


def news(request, topic: str, start_date: str = None, end_date: str = None, **kwargs):
    page_num = int(kwargs.get('Page', '0'))
    article_num = int(kwargs.get('Article', '0'))

    if page_num == 0 and article_num == 0:
        try:
            NewsHistory.objects.latest('search_time').delete()
        except Exception:
            pass

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
    all_articles = "<br>".join([". ".join(i) for i in article_text])

    return {'response': all_articles, 'followup': True}


news = Command(name='news', help_text="""Show the latest news.<br>
Usage: news [search query]<br>
Choose the news article you want to read in the follow up.<br>""",
               action=news)
