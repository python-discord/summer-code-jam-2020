from GoogleNews import GoogleNews

from .models import NewsHistory

import ast

class TerminalCommand():
    """Container for terminal all terminal commands"""

    def __init__(self, option: str):
        self.specified_method = option.split()[0]
        self.params = option[option.find(" ") + 1:]

    def run(self, **kwargs):
        try:
            method_to_call = getattr(self, self.specified_method)
            response = method_to_call(self.params, **kwargs)
        except AttributeError as e:
            response = {'response': f"{self.specified_method}: command not found"}
            print(e)
        return response

    @staticmethod
    def message(params: str = None):
        help_text = "message: use this to send messages<br><br>"\
            "Usage: message username [args] [message text]<br>"\
            "options:<br>"\
            "--help: get help (this screen)<br>"\
            "--e: encrypt the message<br>"\
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
            details = f'{news_details["title"]}<br>{news_details["desc"]}<br><a href="{news_details["link"]}" target="_blank">Read full article</a>'
            return {'response': details}
        articles = []
        start_num = (page_num - 1) * 3
        end_num = page_num * 3
        for i, article in enumerate(news_results[start_num:end_num]):
            serial_number = str(i + 1 + (page_num-1)*3)
            article_summary = (serial_number, f"{article['date']}, {article['media']}", article['title'])
            articles.append(article_summary)
        all_articles = "<br>".join([", ".join(i) for i in articles])
        return {'response': all_articles, 'followup':True}

    @staticmethod
    def news2(topic: str, start_date: str = None, end_date: str = None, **kwargs):
        print(kwargs)
        page_num = kwargs.get('page', 0)
        article_num = kwargs.get('article', None)

        if page_num == 0 and article_num is None:
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
            if page_num is not None:
                # print(page_num)
                article_start_num = (page_num - 1) * 3
                artilces = news_items[article_start_num:article_start_num+3]
            elif article_num is not None:
                article = news_items[article_num - 1]
                article_link = '<a href="{}" target="_blank">Read full article</a>'.format(article['link'])
                article = "<br>".join([article['title'], article['desc'], article_link])
                return {'response': article}
        
        article_text = []
        for i, article in enumerate(articles):
            serial_number = str(i + 1 + (page_num)*3)
            article_summary = (serial_number, f"{article['date']}, {article['media']}", article['title'])
            article_text.append(article_summary)
        all_articles = "<br>".join([", ".join(i) for i in article_text])
        return {'response': all_articles, 'followup': True}

