from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chat-home'),
    path('bot', views.bot, name='chat-bot'),
]