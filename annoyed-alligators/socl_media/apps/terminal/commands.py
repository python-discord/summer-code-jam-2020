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


""" ----- These are the various Terminal Commands ----- """


def help(request, params: str, **kwargs):
    """The help command that lists out all the commands for the user."""

    message = "(Type `[command name] --help` for details of a particular command)<br>Available commands:<br><br>"

    for command in Command.commands_list:
        message += command.name + "<br>"

    return {'response': add_linebreaks(message)}


help = Command(name='help', help_text="""<br>Display a list of all available commands<br>
Usage: help<br>""",
               action=help)


def home(request, params: str, **kwargs):
    redirect = reverse('home')
    message = "Welcome home!"
    messages.success(request, message)
    return {'response': add_linebreaks(message), 'redirect': redirect}


home = Command(name='home', help_text="""<br>Takes you to the home page.<br>
Usage: home<br>""",
               action=home)


def view_post(request, params: str, **kwargs):
    if len(params.split()) < 1:
        message = "Incorrect usage. See: view-post --help"
        return {'response': add_linebreaks(message)}
    else:
        post_id = params.split()[0]
        redirect = reverse('post-detail', args=[post_id])
        message = f"On post {post_id}"
        messages.success(request, message)

    return {'response': add_linebreaks(message), 'redirect': redirect}


view_post = Command(name='view-post', help_text="""<br>View a particular Post.<br>
Usage: view-post [post number]<br>""",
                    action=view_post)


def logout(request, params: str, **kwargs):
    if request.user.is_authenticated:
        redirect = reverse('logout')
        message = f"Logged out {request.user.username}"
        messages.success(request, message)
        return {'response': add_linebreaks(message), 'redirect': redirect}
    else:
        return {'response': add_linebreaks("No user Logged in")}


logout = Command(name='logout', help_text="""<br>Logs out current user.<br>
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


signup = Command(name='signup', help_text="""<br>Register a new user.<br>
Make sure you are logged out to register a new user.<br>
Usage: signup<br>""",
                 action=signup)


def change_password(request, params: str, **kwargs):
    if request.user.is_authenticated:
        redirect = reverse('password_change')
        message = "Change your password."
        messages.success(request, message)
    else:
        message = "No user logged in."
    return {'response': add_linebreaks(message), 'redirect': redirect}


home = Command(name='change-password', help_text="""<br>Change your password.<br>
Usage: change-password<br>""",
               action=change_password)


def message(request, params: str, **kwargs):
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
                    Message.objects.create(body=message_body,
                                           sender=request.user,
                                           recipient=receiver_obj)
                    message = f"Message sent to {receiver_username}"
                else:
                    message = "No message provided. See: message --help"

            except User.DoesNotExist:
                message = f"User '{receiver_username}' does not exist. Enter a valid username."

    return {'response': add_linebreaks(message)}


message = Command(name='message', help_text="""<br>Send a personal message to any user.<br>
Usage: message [username] [message body]""",
                  action=message)


def message_box(request, params: str, **kwargs):
    if not request.user.is_authenticated:
        message = "Log in to view your Message Box"
        return {'response': add_linebreaks(message)}
    else:
        redirect = reverse('message-box')
        message = "Here are your received messages"
        messages.success(request, message)
        return {'response': add_linebreaks(message), 'redirect': redirect}


message_box = Command(name='message-box', help_text="""<br>View your received messages.<br>
Make sure you are logged in to see your messages.<br>
Usage: message-box<br>""",
                      action=message_box)


def profile(request, params: str, **kwargs):
    if not params:
        # Show the logged in user's profile if no other username provided
        message = "Your Profile"
        messages.success(request, message)
        redirect = reverse('profile', args=[request.user.username])

    else:
        username = params.split()[0]

        if username == request.user.username:
            message = "Your Profile"
            messages.success(request, message)
            redirect = reverse('profile', args=[username])
        else:
            try:
                user_obj = User.objects.get(username=username)
                redirect = reverse('profile', args=[user_obj.username])
                message = f"{username}'s Profile"
                messages.success(request, message)
            except User.DoesNotExist:
                message = f"User '{username}' does not exist. Enter a valid username."
                return {'response': add_linebreaks(message)}
    return {'response': add_linebreaks(message), 'redirect': redirect}


profile = Command(name='profile', help_text="""<br>View any user's profile.<br>
Usage: profile [username]""",
                  action=profile)


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


news = Command(name='news', help_text="""<br>Show the latest news.<br>
Usage: news [search query]<br>
Choose the news article you want to read in the follow up.<br>""",
               action=news)
