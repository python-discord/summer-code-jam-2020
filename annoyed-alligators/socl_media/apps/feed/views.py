from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostForm


class PostListView(LoginRequiredMixin, ListView):
    """
    This view is called at the home screen to display all the posts.
    Lists out all the posts in the feed with the latest ones first.
    """

    model = Post
    ordering = ['-post_date_posted']
    paginate_by = 5


class PostDetailView(LoginRequiredMixin, DetailView):
    """
    This view is called to display one particular post.
    """

    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    This view is called to create a new post.
    """

    model = Post
    form_class = PostForm

    def form_valid(self, form, **kwargs):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    This view is called to update the post we want to edit.
    """

    model = Post
    fields = ['post_content', 'post_image']

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.posted_by:
            return True
        else:
            return False


class PostDeleteView(DeleteView):
    """
    This view is called to delete a post.
    """

    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.posted_by:
            return True
        else:
            return False
