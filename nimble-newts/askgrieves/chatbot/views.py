import wikipediaapi
from django.shortcuts import render
from .models import WikiArticle


class Message:
    send = True

    def __init__(self, text):
        if Message.send:
            self.action = 'send'
        else:
            self.action = 'receive'
        Message.send = not self.send
        self.text = text

# Create your views here.


def home(request):
    return render(
        request, 'home.html'
    )


def chat_page(request, bot_name):
    return render(
        request, 'home.html', {'bot': bot_name}
    )


def experimental(request):
    return render(
        request, 'landing_page.html'
    )


def get_wikipedia(request):
    article_name = request.POST.get('article_name')
    if article := WikiArticle.objects.filter(name=article_name):
        # return article
        pass
    else:
        wiki_wiki = wikipediaapi.Wikipedia('en')
        wiki_page = wiki_wiki.page(article_name)
        new_article = WikiArticle(article_name, wiki_wiki.extracts(wiki_page, excsentences=3), wiki_page.text)
        new_article.save()
        # return article
        pass
