import logging

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest

from .models import Project, Comment
from .forms import UserRegisterForm

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


def about(request: HttpRequest) -> HttpResponse:
    """
    Handles feed home GET request
    :param request:
    :return: Feed home with context
    """
    return render(request, 'about.html')


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


def profile(request: HttpRequest) -> HttpResponse:
    """shows profile of the current user"""
    return render(request, 'profile.html')


def detail(request, project_name=None) -> HttpResponse:
    """displays view for project and its comments"""
    # there can only be one
    project = Project.objects.filter(name=project_name, user_id=request.user)[0]
    comments = Comment.objects.filter(post_id=project)
    comment_dict = {}

    list_of_branches = filter(lambda x: x.parent_id is None, comments)

    # def get_branches(branch_list):  represent tree structure of comments as a dictionary
    #     for item in branch_list:
    #         subcomments = filter(lambda x: x.parent_id is item)
    #         comment_dict[item] = {}
    #         get_branches(subcomments)
    return render(request, "project_detail.html", {"project": project, "comments": comments})
