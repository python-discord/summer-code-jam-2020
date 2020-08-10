from django.shortcuts import render
from .forms import CommentForm
from .models import Comment, Video
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string


def index(request):
    comment_form = CommentForm()
    all_videos = Video.objects.all()
    all_comments = Comment.objects.all().order_by('-id')
    total_comments = Comment.objects.all().count()
    paginator = Paginator(all_comments, 5)
    first_page = paginator.page(1).object_list
    page_range = paginator.page_range
    if request.method == 'POST':
        print("successss but first youtube")
    context = {
        'comment_form': comment_form,
        'comments': all_comments,
        'first_page': first_page,
        'page_range': page_range,
        'paginator': paginator,
        'total_comment': total_comments,
        'videos': all_videos
    }

    if request.method == 'POST' and 'page_n' in request.POST:
        page_n = request.POST.get('page_n', None)
        results = list(paginator.page(page_n).object_list.values('id', 'content','publish_date'))
        return JsonResponse({"results": results})

    if request.is_ajax():
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_text = comment_form.cleaned_data.get('content')
            new_comment = Comment()
            new_comment.content = comment_text
            new_comment.save()
            html = render_to_string('first_youtube/comments.html', context, request=request)
            return JsonResponse({
                'message': 'success',
                'form': html
            })

    return render(request, "first_youtube/index.html", context)
