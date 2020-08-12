from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from socl_media.apps.feed.models import Post
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm, UserRegisterForm


def signup(request):
    """
    This view asks new users to sign up.
    (Registers new accounts)
    """

    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'users/signup.html', {'form': form})


class profile(ListView):
    """
    The profile view finds the user passed in the profile url
    and renders their profile page.
    """

    model = Post
    template_name = 'users/profile.html'
    context_object_name = 'posts'

    def get_of_user(self):
        self.of_user = get_object_or_404(User,
                                         username=self.kwargs['username'])
        return self.of_user

    def get_queryset(self):
        of_user = self.get_of_user()
        self.user_posts = Post.objects.filter(
            posted_by=of_user).order_by('-post_date_posted')
        return self.user_posts

    def get_context_data(self, *args, **kwargs):
        context = super(profile, self).get_context_data(*args, **kwargs)
        context['of_user'] = self.get_of_user()
        context['num_posts'] = len(self.user_posts)
        return context


@login_required
def profile_edit(request):
    """
    The view that handles the /profile/edit route and gives the current user
    a form to update their profile info.
    """

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form.save()
            messages.success(request, "Account Information Updated!")
            return redirect('profile', user.username)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile_edit.html', context)
