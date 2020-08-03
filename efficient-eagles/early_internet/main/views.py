from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from .models import Topic, Post
from main.forms import CustomUserCreationForm, TopicCreationForm


class HomeView(TemplateView):
    template_name = 'index.html'


class TopicView(TemplateView):
    template_name = 'topic.html'

    def get(self, request, topic_name):
        topic = Topic.objects.get(topic_name=topic_name.lower())
        posts = Post.objects.filter(topic=topic.id)
        context = {'posts': posts}
        return render(request, self.template_name, context)


class CreateTopicView(TemplateView):
    template_name = 'create_topic.html'

    def get(self, request):
        form = TopicCreationForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TopicCreationForm(request.POST)
        topic_name = form.data.get('topic_name')
        if form.is_valid():
            topic = get_object_or_404(Topic, topic_name=topic_name)
            if topic.topic_name == topic_name:
                context = {'form': form, 'error': 'Topic already Exists'}
                return render(request, self.template_name, context)
            else:
                t = Topic(topic_name=topic_name.lower())
                t.save()
                return redirect('topic/{}'.format(t.topic_name))


class InfoView(TemplateView):
    template_name = 'info.html'

    def get(self, request, topic_name, slug):
        topic = Topic.objects.get(topic_name=topic_name)  # keep these here for the meantime
        post = Post.objects.get(slug=slug)
        context = {
            'post': post
            }
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
