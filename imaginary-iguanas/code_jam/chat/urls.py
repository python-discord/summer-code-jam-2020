from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='chat-index'),
    path('<str:room_name>/', views.room, name='chat-room'),
]
