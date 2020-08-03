from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.db import IntegrityError

from main.models import Topic, Post
from main.forms import CustomUserCreationForm, TopicCreationForm


class HomeView(TemplateView):
    template_name = 'index.html'


class TopicView(TemplateView):
    template_name = 'topic.html'

    def get(self, request, topic_name):
        topic = Topic.objects.get(topic_name=topic_name.lower())
        posts = topic.post_set.all()
        
        context = {'posts': posts}
        return render(request, self.template_name, context)


class CreateTopicView(TemplateView):
    template_name = 'create_topic.html'
    form_class = TopicCreationForm

    def get(self, request):
        form = self.form_class()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = TopicCreationForm(request.POST)
        topic_name = form.data.get('topic_name')
        if form.is_valid():
            try:
                Topic.objects.create(topic_name=topic_name)
            except IntegrityError:
                pass
                
            return redirect('topic', topic_name=topic_name)


class InfoView(TemplateView):
    template_name = 'info.html'

    def get(self, request, topic_name, slug):
        topic = Topic.objects.get(topic_name=topic_name)  # keep these here for the meantime
        post = Post.objects.get(slug=slug)
        context = {'post': post}
        
        return render(request, self.template_name, context)


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
