from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import views as auth_views
from .forms import ForumUserChangeForm, ForumUserCreationForm


def register(request):
    if request.method == 'POST':
        form = ForumUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ForumUserCreationForm()
    return render(request, 'user/register.html', {'form': form})


class Login(auth_views.LoginView):
    template_name = 'user/login.html'


class Logout(auth_views.LogoutView):
    template_name = 'user/logout.html'


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = ForumUserChangeForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
        return redirect('profile')
    else:
        u_form = ForumUserChangeForm(instance=request.user)

    context = {"u_form": u_form}
    return render(request, 'user/profile.html', context)
