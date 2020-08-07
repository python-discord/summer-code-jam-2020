from .models import Post
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class PostList(LoginRequiredMixin, ListView):
    """ 
    Lists out all the posts in the feed.
    """
    model = Post
    queryset = Post.objects.all()
    ordering = ['-post_date_posted']
