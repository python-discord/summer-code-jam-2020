from django.urls import path

from . import views


urlpatterns = [
    path('', views.chat_lobby, name='chat_lobby'),
    path('checkname/', views.check_chat_room_name, name='check_chat_room_name'),
    path('room/<str:room_name>/', views.chat_room, name='chat_room'),
]
