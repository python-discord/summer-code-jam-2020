from django.http import HttpResponse
from django.views.generic import ListView
from django.views import View
from .models import Post, Comments, Community
from django.shortcuts import render
from django.db.models import Count


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

class CommunityView(View):
    template_name = 'community.html'
    model = Community
    context = {}

    def get(self, request, community_name):
        community = self.model.objects.get(name=community_name)
        posts = community.post_publisher.all()
        self.context = {"posts": posts, "community": community}
        return render(request, self.template_name, self.context)

class TopCommunityView(View):
    template_name = 'topcommunity.html'
    model = Community
    context = {}

    def get(self, request):
        communities = self.model.objects.all().annotate(s_count=Count('subscribers')).order_by('-s_count')
        self.context = {"communities": communities}
        return render(request, self.template_name, self.context)
