from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import ForumPost, ForumPostReplyForm


def forum_post(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    reply_list = post.forumpostreply_set.all()

    pages = Paginator(reply_list, 6)

    page_number = request.GET.get('page', 1)
    page_obj = pages.get_page(page_number)

    context = {
        'original_post': post,
        'reply_form': ForumPostReplyForm,
        'page_obj': page_obj
    }

    return render(request, 'forum/forum_post.html', context)


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
