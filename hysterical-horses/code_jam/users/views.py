from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import View
from users.mixins import LevelRestrictionMixin

from .forms import AccountCreationForm, ProfileUpdateForm, UserUpdateForm


class ProfileView(LevelRestrictionMixin, View):
    template_name = "users/profile.html"

    def test_func(self):
        return self.request.user.profile_change_unlocked

    def get(self, request):
        return render(self.request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")

    def get_context_data(self, **kwargs):
        user_form = UserUpdateForm(instance=self.request.user)
        profile_form = ProfileUpdateForm(instance=self.request.user.profile)

        context = {
            "user_form": user_form,
            "profile_form": profile_form,
            "user": self.request.user,
        }
        return context


def signup_view(request):
    form = AccountCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_password)
        login(request, user)  # Immediately log the user in
        return redirect("dashboard-index")

    context = {"form": form}
    return render(request, "users/signup.html", context)
