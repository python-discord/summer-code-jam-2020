from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from random import randint
from collections.abc import Iterable
from django.db.models import Q
from .models import UserVote
from .forms import CreateUserForm, ProfileUpdateForm, UserUpdateForm
from .decorators import unauthenticated_user, allowed_users


# Create your views here.
def home(request):
    return render(request, 'dating/home.html')


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.last_login is None:
            login(request, user)
            return redirect('earlydating-editprofile')
        elif user is not None:
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


@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
def DateMatcher(request):
    logged_user = request.user
    if request.method == 'POST':
        print(request.POST)
        if like_pk := request.POST.get('Like'):
            voted = User.objects.get(pk=like_pk)
            vote, _ = UserVote.objects.get_or_create(user=voted, voter=logged_user)
            vote.vote = True
        elif like_pk := request.POST.get('Unlike'):
            voted = User.objects.get(pk=like_pk)
            vote, _ = UserVote.objects.get_or_create(user=voted, voter=logged_user)
            vote.vote = False
        vote.save()
        return redirect('earlydating-profile', pk=like_pk)
    elif request.method == 'GET':
        user = get_unvoted(logged_user)[0]
        return redirect('earlydating-profile', pk=user.pk)


def getfilters(user):
    u_sex = user.profile.sex
    gender = ['Male', 'Female']
    try:
        if user.profile.preference == 'straight':
            Q1 = Q(profile__sex=gender[int(not gender.index(u_sex))])
            Q2 = Q(profile__preference__in=['straight', 'bisexual'])
            return Q1 & Q2

        elif user.profile.preference == 'gay':
            Q1 = Q(profile__sex=u_sex)
            Q2 = Q(profile__preference__in=['gay', 'bisexual'])
            return Q1 & Q2

        elif user.profile.preference == 'bisexual':
            Q1 = Q(profile__sex=u_sex)
            Q2 = Q(profile__preference='gay')
            Q3 = Q(profile__sex=gender[int(not gender.index(u_sex))])
            Q4 = Q(profile__preference='straight')
            Q5 = Q(profile__preference='bisexual')
            return (Q1 & Q2) | (Q3 & Q4) | Q5

    except Exception as e:
        print(e)
        return None


def get_unvoted(voter, num=1):
    try:
        votes = UserVote.objects.filter(voter=voter, vote=True)
        if not isinstance(votes, Iterable):
            votes = [votes]
        voted_pk = [vote.user.pk for vote in votes] + [voter.pk]
    except UserVote.DoesNotExist:
        voted_pk = [voter.pk]
    unvoted = User.objects.exclude(pk__in=voted_pk)
    if (filter := getfilters(voter)) is not None:
        unvoted = unvoted.filter(filter)
    return unvoted.order_by('?')[:num]


@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
def likedmatches(request):
    logged_user = request.user
    liked_you = UserVote.objects.filter(user=logged_user, vote=1).exclude(voter=logged_user)
    you_liked = UserVote.objects.filter(voter=logged_user, vote=1).exclude(user=logged_user)
    page_likes = Paginator(liked_you, 9)
    page_liked = Paginator(you_liked, 9)

    page_number = request.GET.get('page')
    page_obj_likes = page_likes.get_page(page_number)
    page_obj_liked = page_liked.get_page(page_number)

    context = {'liked_you': liked_you, 'you_liked': you_liked,
               'obj_liked': page_obj_liked, 'obj_likes': page_obj_likes}
    return render(request, 'dating/mylikes.html', context)


@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
def bothliked(request):
    logged_user = request.user
    liked_you = UserVote.objects.filter(user=logged_user, vote=True).exclude(voter=logged_user)
    you_liked = UserVote.objects.filter(voter=logged_user, vote=True).exclude(user=logged_user)
    both_liked = liked_you.intersection(you_liked)
    whole_list = liked_you.union(you_liked)
    context = {'liked_you': liked_you, 'you_liked': you_liked, 'both_liked': both_liked, 'everyone': whole_list}

    return render(request, 'dating/bothlikes.html', context)


@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
def profile(request, pk):
    logged_user = request.user
    user = User.objects.get(pk=pk)
    try:
        like = UserVote.objects.get(user=user, voter=logged_user).vote
    except UserVote.DoesNotExist:
        like = False
    context = {'current': user, 'like': like}
    return render(request, 'dating/profile.html', context)


@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
def your_profile(request):
    profile = request.user
    num_likebacks = randint(2, 5)
    other_users = get_unvoted(profile, num_likebacks)
    for other_user in other_users:
        votes, created = UserVote.objects.get_or_create(user=profile, voter=other_user, vote=True)
        if created:
            votes.vote = not votes.vote
    context = {'profile': profile}
    return render(request, 'dating/YourProfile.html', context)
