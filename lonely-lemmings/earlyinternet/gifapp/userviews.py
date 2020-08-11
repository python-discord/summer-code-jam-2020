import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest

from .models import Project, Comment
from .forms import UserRegisterForm, CommentForm

logger = logging.getLogger(__name__)


def home(request: HttpRequest) -> HttpResponse:
    """
    Handles feed home GET request
    :param request:
    :return: Feed home with context
    """
    context = {
        "feed": Project.objects.exclude(upload_version="")
    }
    return render(request, 'home.html', context)


def register(request: HttpRequest) -> HttpResponse:
    """
    Handles register endpoint POST request
    :param request: HttpRequest object containing form data for registering a new user
    :return: redirect if successful account formation, else the same RegisterForm
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


def detail(request, user=None, project_name=None) -> HttpResponse:
    """displays view for project and its comments"""

    # there can only be one
    # Comments removed for now
    project = Project.objects.filter(name=project_name, user_id__username=user)[0]
    comments = Comment.objects.filter(post_id=project)

    return render(request, "project_detail.html", {"project": project, "comments": comments, "form": CommentForm()})


@login_required
def submit_comment(request, user=None, project_name=None) -> HttpResponse:
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            project = Project.objects.filter(name=project_name, user_id__username=user)[0]
            Comment.objects.create(content=content, post_id=project, user_id=request.user)

    # go back to detail view
    return detail(request, user, project_name)
