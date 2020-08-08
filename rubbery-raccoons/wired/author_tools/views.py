from datetime import date

from django.contrib import messages
from django.shortcuts import render
from django.utils.text import slugify

from .forms import ArticleForm, CommentForm


def compose(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.author = request.user
            art.publication_date = date.today()
            art.slug = "-".join(
                (slugify(x) for x in [art.author.username, art.title, art.publication_date])
            )
            art.save()
            messages.success(request, "Article submitted!")
        else:
            messages.error(request, "Form input was invalid.")

    else:
        form = ArticleForm()

    return render(request, "author_tools/compose.html", {"form": form})
