from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'first_twitter/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']