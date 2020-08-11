from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile, FriendRequest


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created! You are now able to log in.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect("profile")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"u_form": u_form, "p_form": p_form}

    return render(request, "users/profile.html", context)


@login_required
def send_request(request, id):
    from_user = Profile.objects.get(user=request.user)
    to_user = Profile.objects.get(id=id)
    FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)  # created
    return redirect("blog-home")


@login_required
def accept_request(request, id):
    frequest = FriendRequest.objects.get(id=id)
    user1 = Profile.objects.get(user=request.user)
    user2 = frequest.from_user  # this from_user is a profile
    user1.friends.add(user2)
    user2.friends.add(user1)
    return redirect("blog-home")
