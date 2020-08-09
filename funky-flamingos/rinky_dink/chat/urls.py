from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='chat_index'),
    path('get_messages', views.get_messages, name='get_messages'),
    path('send_message', views.send_message, name='send_message'),
]
