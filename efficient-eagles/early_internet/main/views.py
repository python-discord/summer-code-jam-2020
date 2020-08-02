from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


User = get_user_model()

class HomeView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        template_name = "index.html"
        return render(request, 'index.html')


class Login(TemplateView):
    template_name = 'registration/login.html'

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')

        return render(request, 'registration/login.html', {})


class Register(TemplateView):
    template_name = 'signup.html'

    def post(self, request):
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('home')
                else:
                    return redirect('signup')
            else:
                form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})


class Logout(TemplateView):

    def get(self, request):
        auth.logout(request)
        return render('registration/home.html')
