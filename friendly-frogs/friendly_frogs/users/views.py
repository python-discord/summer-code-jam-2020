from django.shortcuts import render
from .forms import UserRegisterForm, ProfileForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        form_p = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid() and form_p.is_valid():
            form.save()
            form_p.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account successfully created for {username}")
    else:
        form = UserRegisterForm()
        form_p = ProfileForm
    context = {'form': form, 'form_p': form_p}
    return render(request, "users/register.html", context)
