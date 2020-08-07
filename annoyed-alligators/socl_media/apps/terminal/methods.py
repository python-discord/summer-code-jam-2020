from django.shortcuts import redirect
from django.urls import reverse
from GoogleNews import GoogleNews


class TerminalCommand():
    """Container for terminal all terminal commands"""

    def __init__(self, command_string: str, request):
        self.specified_method = command_string.split()[0]
        self.params = command_string[command_string.find(" ") + 1:]
        self.request = request

    def run(self):
        try:
            method_to_call = getattr(self, self.specified_method)
            response = method_to_call(self.params)
        except AttributeError as e:
            response = {'response': f"{self.specified_method}: command not found"}
        return response

    def logout(self, params=None):
        redirect = reverse('logout')
        message = f"Logged out {self.request.user.username}"
        return {'response': message, 'redirect': redirect}

    def signup(self, params=None):
        if self.request.user.is_authenticated:
            message = "Log out to create a new account"
            return {'response': message}
        else:
            redirect = reverse('signup')
            message = "enter details to signup"
            return {'response': message, 'redirect': redirect}

    @staticmethod
    def message(params: str = None):
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
    def news(topic: str, start_date: str = None, end_date: str = None):
        help_text = "news: use this to fetch news<br><br>"\
            "Usage: news topic<br>"\
            "options:<br>"\
            "--help: get help (this screen)<br><br>"\
            "Followup: After fetching a set of news articles, enter<br>"\
            "n: fetch the next set of articles<br>"\
            "number: fetch the details of the article"

        googlenews = GoogleNews()
        page_num = 1
        detail = None
        if start_date is not None and end_date is not None:
            googlenews.setTimeRange(start_date, end_date)
        if topic.split()[0] == '--help':
            return {'response': help_text}
        if topic.count('~') > 0:
            followup = topic.split('~')[1]
            if followup.split()[0] == 'n':
                page_num = int(followup.split()[1]) + 1
                print(f"Page number: {page_num}")
            elif followup.split()[0].isnumeric():
                detail = int(followup.split()[0])
            topic = topic.split('~')[0]
        googlenews.search(topic)
        googlenews.getpage(1)
        news_results = googlenews.result()
        if detail is not None:
            news_details = news_results[detail + 1]
            print(news_details)
            details = f'{news_details["title"]}<br>{news_details["desc"]}<br>'\
                '<a href="{news_details["link"]}" target="_blank">Read full article</a>'
            return {'response': details}
        articles = []
        start_num = (page_num - 1) * 3
        end_num = page_num * 3
        for i, article in enumerate(news_results[start_num:end_num]):
            serial_number = str(i + 1 + (page_num-1)*3)
            article_summary = (serial_number, f"{article['date']}, {article['media']}", article['title'])
            articles.append(article_summary)
        all_articles = "<br>".join([", ".join(i) for i in articles])
        return {'response': all_articles, 'followup': True}
