
from django.urls import path

from . import views

app_name = 'nchan'
urlpatterns= [
    path('get_boards', views.get_boards),
    path('add_board', views.add_board),
    path('', views.index),
]