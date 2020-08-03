from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='chat-home'),
    path('chat/', views.chat, name='chat'),
]