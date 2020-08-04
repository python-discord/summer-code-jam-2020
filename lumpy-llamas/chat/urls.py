from django.urls import path

from . import views


urlpatterns = [
    path('', views.chat_lobby, name='chat_lobby'),
    path('<str:room_name>/', views.chat_room, name='chat_room'),
]
