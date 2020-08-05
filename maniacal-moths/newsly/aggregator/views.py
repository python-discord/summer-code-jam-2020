from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


def home(request):
    context = {"articles": Article.objects.all()}
    return render(request, "aggregator/home.html", context)


class ArticleListView(ListView):
    model = Article
    template_name = "aggregator/home.html"
    context_object_name = "articles"
    ordering = ["-date_posted"]  # Latest Posts First


class ArticleDetailView(DetailView):
    model = Article


def about(request):
    return render(request, "aggregator/about.html", {"title": "About"})
