from django.http import HttpResponse
from django.views.generic import ListView
from django.views import View
from .models import Post, Comments
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth

def index(request):
    return HttpResponse("Hello, world. You're at the Syndication index.")


class IndexListView(ListView):
    paginate_by = 25
    template_name = "index.html"
    queryset = Post.objects.all()


class PostView(View):
    template_name = 'single-post.html'
    model = Post
    context = {}

    def get(self, request, community_name, post_id):
        post = self.model.objects.get(id=post_id)
        comments = post.comment_post.all()
        self.context = {"comments": comments, "post": post}
        return render(request, self.template_name, self.context)


def login_request(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')

def logout_request(request):
    auth.logout(request)
    return redirect('/')