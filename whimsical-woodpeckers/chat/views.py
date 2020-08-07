from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Text


def home(request):
    return render(request, 'chat/home.html')

class PostListView(LoginRequiredMixin, ListView):
    model = Text
    template_name = 'chat/chat.html'
    context_object_name = 'texts'
    ordering = ['date_sent']

class PostDetailView(DetailView):
    model = Text

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Text
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Text
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        text = self.get_object()
        if self.request.user == text.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Text
    success_url = '/chat'

    def test_func(self):
        text = self.get_object()
        if self.request.user == text.author:
            return True
        return False