from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<room_name>\w+)/', views.room, name='chat'),
]
