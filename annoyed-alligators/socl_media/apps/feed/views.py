from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    """
    This view is called at the home screen to display all the posts.
    Lists out all the posts in the feed with the latest ones first.
    """
    model = Post
    ordering = ['-post_date_posted']


class PostDetailView(LoginRequiredMixin, DetailView):
    """
    This view is called at the home screen to display all the posts.
    Lists out all the posts in the feed with the latest ones first.
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    This view is called to create a new post.
    """
    model = Post
    fields = ['post_content']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    This view is called to update the post we want to edit.
    """
    model = Post
    fields = ['post_content']
    success_url = "/"


class PostDeleteView(DeleteView):
    """
    This view is called to delete the post we want.
    """

    model = Post
    success_url = "/"
