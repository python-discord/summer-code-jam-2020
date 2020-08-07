from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post


class PostList(LoginRequiredMixin, ListView):
    """ 
    This view is called at the home screen to display all the posts.
    Lists out all the posts in the feed with the latest ones first.
    """
    model = Post
    queryset = Post.objects.all()
    ordering = ['-post_date_posted']
