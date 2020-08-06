from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .filters import PostFilter
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'blogs_list.html'

    filterset_class = PostFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(
            self.request.GET, queryset=queryset
        )
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"
