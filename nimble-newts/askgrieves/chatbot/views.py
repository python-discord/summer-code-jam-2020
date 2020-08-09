from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import Http404, JsonResponse
from django.shortcuts import render
from .models import WikiArticle

from wikipediaapi import Wikipedia


class Message:
    send = True

    def __init__(self, text):
        if Message.send:
            self.action = 'send'
        else:
            self.action = 'receive'
        Message.send = not self.send
        self.text = text


def home(request):
    return render(request, 'home.html')


def chat_page(request, bot_name):
    return render(request, 'home.html', {'bot': bot_name})


def experimental(request):
    return render(request, 'landing_page.html')


def get_wikipedia(request):
    article_name = request.POST.get('article_name')
    try:
        article = WikiArticle.objects.get(name=article_name)
        serialied_article = model_to_dict(article, fields=('name', 'summary'))
    except ObjectDoesNotExist:
        wiki_wiki = Wikipedia('en')
        wiki_page = wiki_wiki.page(article_name)
        if not wiki_page.exists():
            raise Http404('Wiki page does not exist')
        new_article = WikiArticle.objects.create(name=article_name,
                                                 summary=wiki_wiki.extracts(wiki_page, excsentences=3),
                                                 full_page=wiki_page.text)
        serialied_article = model_to_dict(new_article, fields=('name', 'summary'))
    return JsonResponse(serialied_article)
