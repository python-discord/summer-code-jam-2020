from django.contrib import messages
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from wired_app.models import Article, Comment
from wired_app.forms import CommentForm


def article_detail_view(request, slug):
    art = get_object_or_404(Article, slug=slug)
    art_dict = model_to_dict(art)
    art_dict["author"] = art.author.username
    comments = Comment.objects.filter(parent_post=art).order_by("created")

    if request.method == "POST":  # a comment was submitted
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user if request.user.is_authenticated else None
            comment.parent_post = art
            messages.success(request, "Comment submitted! Thank you.")
            comment.save()
            form = CommentForm()
        else:
            messages.error(request, "Form input was invalid.")
    else:
        form = CommentForm()

    context = {"art": art_dict, "comments": comments, "now": timezone.now(), "form": form}

    return render(request, "wired_app/article_detail.html", context)
