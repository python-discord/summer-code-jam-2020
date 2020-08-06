from django.shortcuts import render, redirect
# from .models import Profile
from .forms import CreateUserForm, ProfileUpdateForm, UserUpdateForm
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm


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

# MADE TO AUTOMATICALLY PUT SIGNED USERS IN MAYBE SIMPLER
# def register(request):
#     if request.method == 'Post':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account Made | Get Loving {username}!')
#             return redirect('earlydating-DateMatcher')
#         else:
#             form= CreateUserForm()
#         return redirect('earlydating-DateMatcher')


def logoutUser(request):
    logout(request)
    return redirect('earlydating-login')


def about(request):
    return render(request, 'dating/about.html')


@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
def DateMatcher(request):
    return render(request, 'dating/DateMatcher.html')


@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
def your_profile(request):
    profile = request.user
    context = {'profile': profile}
    return render(request, 'dating/YourProfile.html', context)


class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'dating/edit_profile.html'
    success_url = reverse_lazy('')

    def get_object(self):
        return self.request.user


@login_required(login_url='earlydating-login')
@allowed_users(allowed_roles=['profile'])
def editprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated.')
            return redirect('../YourProfile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile) 

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'dating/edit_profile.html', context)
