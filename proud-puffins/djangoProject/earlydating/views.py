from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from .models import UserVote
from .forms import CreateUserForm, ProfileUpdateForm, UserUpdateForm
from .decorators import unauthenticated_user, allowed_users
from random import randint
from collections.abc import Iterable


# Create your views here.
def home(request):
    return render(request, 'dating/home.html')


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('earlydating-yourprofile')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {'form': AuthenticationForm()}
    return render(request, 'dating/login.html', context)


@unauthenticated_user
def register_page(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('earlydating-login')
    context = {'form': form}
    return render(request, 'dating/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('earlydating-login')


def about(request):
    return render(request, 'dating/about.html')


@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
def editprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('../YourProfile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'dating/edit_profile.html', context)

#### WORK IN PROCESS : Below is the list of views for creating user matches ####

@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
def DateMatcher(request):
    logged_user = request.user
    if request.method == 'POST':
        print(request.POST)
        if liked_pk := request.POST.get('Like'):
            voted = User.objects.get(pk=liked_pk)
            UserVote.objects.get_or_create(user=voted, voter=logged_user, vote=True)

        return redirect('earlydating-DateMatcher')
    elif request.method == 'GET':

        user = get_unvoted(logged_user)
        context = {'current': user}
        return render(request, 'dating/DateMatcher.html', context)


def get_unvoted(voter):
    try:
        votes = UserVote.objects.filter(voter=voter)
        if not isinstance(votes, Iterable):
            votes = [votes]
        voted_pk = [vote.user.pk for vote in votes] + [voter.pk]
    except UserVote.DoesNotExist:
        voted_pk = [voter.pk]
    unvoted = User.objects.exclude(pk__in=voted_pk).order_by('?')[0]
    return unvoted


@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
def Matches(request):
    logged_user = request.user
    liked_you = UserVote.objects.filter(user=logged_user).exclude(voter=logged_user)
    you_liked = UserVote.objects.filter(voter=logged_user).exclude(user=logged_user)
    both_liked = liked_you.intersection(you_liked)
    whole_list = liked_you.union(you_liked)
    context = {'liked_you': liked_you, 'you_liked': you_liked, 'both_liked': both_liked, 'everyone': whole_list}
    return render(request, 'dating/matches.html', context)


@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
def your_profile(request):
    profile = request.user
    num_likebacks = randint(2, 5)
    other_users = User.objects.exclude(pk=profile.pk).order_by('?')[:num_likebacks]
    for other_user in other_users:
        votes, created = UserVote.objects.get_or_create(user=profile, voter=other_user, vote=True)
        if created:
            votes.vote = not votes.vote
    context = {'profile': profile}
    return render(request, 'dating/YourProfile.html', context)
