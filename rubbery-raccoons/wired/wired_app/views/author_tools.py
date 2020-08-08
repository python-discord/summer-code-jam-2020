from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from wired_app.models import Article


def author_main(request):
    return render(request, "wired_app/author_main_portal.html")


def author_compose(request):
    return HttpResponse("This is the author compose page.")


def author_edit(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "wired_app/author_main_portal.html", {"question": question})
