from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import MediaFile, ForumPost, ForumPostReplyForm
from .forms import MediaUploadForm, PostSearchForm


def forum_post(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    reply_list = post.forumpostreply_set.all().order_by("created_at")

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
            return HttpResponseRedirect(f'/forum/{post_id}?page=-1')
    else:
        form = ForumPostReplyForm()

    return render(request, f'forum/{post_id}')


def index(request):
    # TODO: confirm if dates in descending order mean newest first
    post_list = ForumPost.objects.order_by('-created_at')
    context = {
        'post_list': post_list,
        'top_post': post_list.order_by('-rating').first(),
        'search': PostSearchForm()
    }

    return render(request, 'forum/index.html', context)


def enter_media(requestObj):
    """ Helper for upload_post(), process media uploads for post creation """
    video_extensions = (
        '.mpeg',
        '.mp4',
        '.mov'
    )
    uploadedFile = requestObj.FILES['media_file']

    media_entry = MediaFile.objects.create(
        data=uploadedFile,
        is_video=uploadedFile.name.endswith(video_extensions)
    )
    media_entry.save()

    return media_entry


def upload_post(request):
    if request.method == "POST":
        form = MediaUploadForm(request.POST)
        if form.is_valid():
            media_entry = enter_media(request)
            entry = ForumPost.objects.create(media_file=media_entry, **request.POST)
            entry.save()

            if ForumPost.objects.get(pk=entry.id):
                return HttpResponseRedirect(f'/forum/{entry.id}?page=-1')
            else:
                return HttpResponseRedirect('/')
        else:
            return render(request, 'forum/upload_error.html', {'errors': form.errors})

    else:
        return render(request, 'forum/upload.html', {'upload_form': MediaUploadForm()})


def search_posts(request):
    search_parameters = [fieldname for fieldname in ForumPost.fields()]
    result_set = set()

    for keyword in search_parameters:
        kwarg = {f'{keyword}__icontains': request.POST['search_string']}
        intermediate_result = ForumPost.objects.filter(**kwarg)

        for post in intermediate_result:
            result_set.add(post)

    if len(result_set) == 0:
        return render(request, 'forum/search_no_results.html')

    context = {
        'results': list(result_set),
        'search_string': request.POST['search_string']
    }

    return render(request, 'forum/search.html', context)


def vote_post(request, post_id, vote_up):
    # TODO: needs to be implemented into the template
    post = get_object_or_404(ForumPost, id=post_id)
    if vote_up:
        post.rating += 1
    else:
        post.rating -= 1

    pages = Paginator(post.objects.forumpostreply_set, 6)

    page_number = request.GET.get('page', 1)
    page_obj = pages.get_page(page_number)

    context = {
        'original_post': post,
        'reply_form': ForumPostReplyForm,
        'page_obj': page_obj
    }

    return render(request, 'forum/forum_post_after_vote.html', context)
