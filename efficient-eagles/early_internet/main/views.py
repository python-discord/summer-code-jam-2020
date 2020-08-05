import random

from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.urls import reverse
from django.db import IntegrityError

from main.models import Topic, Post
from main.forms import CustomUserCreationForm, TopicCreationForm, PostForm, CustomUser


class HomeView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        posts = Post.objects.values_list("id", flat=True)
        random_profiles_id_list = random.sample(list(posts), min(len(posts), 10))
        query_set = Post.objects.filter(id__in=random_profiles_id_list)
        context = {"posts": query_set}
        return render(request, self.template_name, context)

    def post(self, request):
        query = request.POST["query"]
        return redirect(reverse("search", args=[query]))


class CreatePostView(TemplateView):
    template_name = "create_post.html"
    form_class = PostForm

    def get(self, request):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            topic_id = request.POST.get("topic")
            title = request.POST.get("title")
            body = request.POST.get("body")
            author = request.user

            topic = Topic.objects.get(pk=topic_id)
            Post.objects.create(title=title, author=author, body=body, topic=topic)
            return redirect("topic", name=topic.name)


class TopicView(TemplateView):
    template_name = "topic.html"

    def get(self, request, name):
        topic = get_object_or_404(Topic, name=name.lower())
        posts = topic.post_set.all()

        context = {"posts": posts, "topic": topic}
        return render(request, self.template_name, context)

    def post(self, request):
        if "query" in request.POST:
            query = request.POST["query"]
            return redirect(reverse("search", args=[query]))


class CreateTopicView(TemplateView):
    template_name = "create_topic.html"
    form_class = TopicCreationForm

    def get(self, request):
        form = self.form_class()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = TopicCreationForm(request.POST)
        name = form.data.get("name")
        if form.is_valid():
            try:
                Topic.objects.create(name=name.lower())
            except IntegrityError:
                context = {"form": form, "error": "Topic already exists"}
                return render(request, self.template_name, context)

            return redirect("topic", name=name)


class InfoView(TemplateView):
    template_name = "info.html"

    def get(self, request, *args, **kwargs):
        topic = Topic.objects.get(name=kwargs["name"].lower())
        post = Post.objects.get(slug=kwargs["slug"])
        context = {"post": post, "topic": topic}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if "query" in request.POST:
            query = request.POST["query"]
            return redirect(reverse("search", args=[query]))

        elif "delete" in request.POST:
            post_id = get_object_or_404(Post, id=request.POST.get("post_id"))
            post_id.delete()
            return redirect("topic", name=kwargs["name"])


class LoginView(TemplateView):
    template_name = "registration/login.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")

        return render(request, self.template_name, {})


class RegisterView(View):
    form_class = CustomUserCreationForm
    template_name = "register.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("home")

            return redirect("register")

        form = self.form_class()
        return render(request, self.template_name, {"form": form})


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect("home")


class SearchView(TemplateView):
    template_name = "search.html"

    def get(self, request, q):
        posts = Post.objects.filter(title__contains=q)
        context = {"posts": posts}
        return render(request, self.template_name, context)

    def post(self, request, q):
        query = request.POST["query"]
        return redirect(reverse("search", args=[query]))


class UserView(TemplateView):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, username=kwargs['user'])
        posts = Post.objects.filter(author=user.id)
        context = {'user': user, 'posts': posts}
        return render(request, self.template_name, context)
