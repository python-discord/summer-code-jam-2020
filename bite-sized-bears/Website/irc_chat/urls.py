from django.urls import path, re_path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^<str:room_name>/chat/', views.room, name='chat'),
]
