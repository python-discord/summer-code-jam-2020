from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ImagePost


class ImagePostListView(ListView):
    model = ImagePost
    template_name = "posts/home.html"
    context_object_name = "posts"
    ordering = ["-date"]
    paginate_by = 16


class ImagePostDetailView(DetailView):
    model = ImagePost
    template_name = "posts/imagepost.html"
