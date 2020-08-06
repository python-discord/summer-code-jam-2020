from django.shortcuts import render, redirect
from .models import UserVote
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
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
def DateMatcher(request):
    logged_user = request.user
    if request.method == 'GET':
        if liked_pk := request.GET.get('Like'):
            voted = User.objects.get(pk=liked_pk)
            UserVote.objects.get_or_create(user=voted, voter=logged_user, vote=True)
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


@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'dating/edit_profile.html'
    success_url = reverse_lazy('')

    def get_object(self):
        return self.request.user
