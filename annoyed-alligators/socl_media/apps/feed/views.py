# from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.utils.decorators import method_decorator

# Create your views here.


# @login_required
# def feed(request):

#     """
#     This view shows posts
#     for the logged in user.

#     """
#     posts_object = Post.objects.all()
#     posts_list = []
#     for post in posts_object:
#         post_struct = {'Content': post.post_content,
#                        'Author': post.posted_by,
#                        'Date': post.post_date_posted}
#         posts_list.append(post_struct)
#     context = {"Feed": posts_list}
#     return render(request, 'feed/home.html', context=context)

@method_decorator(login_required, name="dispatch")
class PostList(ListView):
    model = Post
    # template_name = "feed/Post_list.html"
    queryset = Post.objects.all()
