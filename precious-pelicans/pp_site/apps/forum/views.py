from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import ForumPost, ForumPostReplyForm


def forum_post(request, post_id, form=None):
    post = ForumPost.objects.get(id=post_id)
    reply_list = post.forumpostreply_set.all()
    context = {
        'original_post': post,
        'replies': reply_list,
        'reply_form': form or ForumPostReplyForm
    }

    return render(request, 'forum/post-template.html', context)


def forum_post_reply(request, post_id):
    if request.method == "POST":
        form = ForumPostReplyForm(
            data=request.POST
        )

        if form.is_valid():
            forum_reply = form.save(commit=False)
            forum_reply.forum_post = ForumPost.objects.get(id=post_id)
            forum_reply.forum_post_id = post_id
            forum_reply.save()
            return HttpResponseRedirect(f'/forum/{post_id}')
    else:
        form = ForumPostReplyForm()

    # TODO: fix this so that it renders the page with form filled in
    return render(request, f'forum/{post_id}')


def index(request):
    post_list = ForumPost.objects.all()
    context = {
        'post_list': post_list
    }

    return render(request, 'forum/index.html', context)
