from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('<str:room_name>/', views.room, name='room'),
    url(r'^(?P<room_name>[\w]+)/', views.room, name='chat'),

]
