from django.urls import path
from . import views


urlpatterns = [
    path('', views.music_player, name='music-home'),
    path('delete_music/<int:pk>', views.delete_music, name='music-delete'),
    path('use_music/<int:pk>', views.use_music, name='music-use'),
    path('add_music/', views.add_music, name='add-music')
]
