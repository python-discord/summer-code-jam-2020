from django.shortcuts import render
from .models import ForumPostOriginal


def post(request, PostId):

    post = ForumPostOriginal.objects.get(id=PostId)
    media = post.content
    replyList = post.forumpostreply_set.all()
    context = {
        'originalPost': post,
        'replies': replyList,
        'media': media
    }
    return render(request, 'forum/post-template.html', context)


def index(request):
    postList = ForumPostOriginal.objects.all()
    context = {
        'postList': postList
    }
    return render(request, 'forum/index.html', context)
