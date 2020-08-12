from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_feed, name='news-feed'),


]
