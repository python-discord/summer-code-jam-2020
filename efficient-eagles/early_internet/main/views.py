from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from main.forms import CustomUserCreationForm


class HomeView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'registration/login.html'

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')

        return render(request, self.template_name, {})


class RegisterView(View):
    form_class = CustomUserCreationForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')

            return redirect('register')

        form = self.form_class()
        return render(request, self.template_name, {'form': form})


class LogoutView(View):

    def get(self, request):
        auth.logout(request)
        return redirect('home')
