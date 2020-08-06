from django.shortcuts import render
from django.contrib.auth.models import User
from .news_api import get_news_from_newsapi
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, *args, **kwargs):
		context = super(IndexView, self).get_context_data(*args, **kwargs)
		source='bbc-news'
		context['news'] = get_news_from_newsapi(source)
		return context