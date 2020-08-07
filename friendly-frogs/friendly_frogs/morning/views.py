from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .apis_call import News
from users.models import Profile


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'morning/index1.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        user = self.request.user
        source = Profile.objects.get(user=user).news_source
        news = News()
        context['news'] = news.get_news(source)['articles']
        return context


def index(request):
    return render(request, "morning/index.html")
