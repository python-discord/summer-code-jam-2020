from .models import Post
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class PostList(LoginRequiredMixin, ListView):
    """
    This view is used for creating
    posts and showring posts in th feed.
    """
    model = Post
    queryset = Post.objects.all()
