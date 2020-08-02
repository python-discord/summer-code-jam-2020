from django.urls import path
from . import views

urlpatterns = [
    path('', views.music_player, name='music-home'),
    path('add_music/', views.add_music, name='add-music')
]
