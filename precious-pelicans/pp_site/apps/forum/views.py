from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import ForumPost, ForumPostReplyForm, ForumPostForm, ForumMedia
from .forms import PostSearchForm
import shlex
import re


def forum_post(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    reply_list = post.forumpostreply_set.all().order_by("created_at")

    pages = Paginator(reply_list, 6)

    page_number = request.GET.get('page', 1)
    page_obj = pages.get_page(page_number)

    context = {
        'original_post': post,
        'reply_form': ForumPostReplyForm,
        'page_obj': page_obj,
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
            return HttpResponseRedirect(f'/forum/{post_id}?page=-1')

    return render(request, f'forum/{post_id}')


def index(request):
    if ForumPost.objects.count() == 0:
        return render(request, 'forum/indexempty.html')

    post_list = ForumPost.objects.order_by('-created_at')
    context = {
        'post_list': post_list,
        'top_post': post_list.order_by('-rating').first(),
        'search': PostSearchForm()
    }

    return render(request, 'forum/index.html', context)


def get_file_ext(uploaded_file):
    return uploaded_file.name.split('.')[-1]


def upload_post(request):
    if request.method == "POST":
        form = ForumPostForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            if get_file_ext(request.FILES["media_file"]) in ForumMedia.video_types:
                saved_post.is_video = True
                saved_post.save()

            return HttpResponseRedirect(f'/forum/{saved_post.id}')
        return render(request, 'forum/upload_error.html', {'errors': form.errors})
    return render(request, 'forum/upload.html', {'upload_form': ForumPostForm})


def normalize_query(query_string):
    # Remove extra spaces
    query_string = re.sub(' +', ' ', query_string)

    # Split while keeping quoted sub-strings
    return shlex.split(query_string)


def get_query(query_string, search_field):
    query = None
    terms = normalize_query(query_string)

    # For each search term it generates a query for each field, this query is then added to the main query
    for term in terms:
        term_query = None
        for field_name in search_field:
            q = Q(**{f"{field_name}__icontains": term})

            if term_query is None:
                term_query = q
            else:
                term_query |= q

        if query is None:
            query = term_query
        else:
            query &= term_query

    return query


def search_posts(request):
    search_string = request.POST['search_string']
    query = get_query(search_string, ("title", "author", "description"))

    results = ForumPost.objects.filter(query).order_by("-created_at")

    if len(results) == 0:
        return render(request, 'forum/search_no_results.html')

    context = {
        'search_results': results,
        'search_string': request.POST['search_string']
    }

    return render(request, 'forum/search.html', context)


def vote_post(request, post_id):
    post = get_object_or_404(ForumPost.objects, id=post_id)
    if request.POST['vote'] == 'up':
        post.rating += 1
    else:
        post.rating -= 1

    post.save()

    return redirect(f'/forum/{post_id}')
