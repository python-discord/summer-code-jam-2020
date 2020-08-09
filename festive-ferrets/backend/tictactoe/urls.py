from django.urls import path

from . import views

app_name = 'tictactoe'
urlpatterns = [
    path('start-play', views.start_playing),
    path('preview', views.get_preview),
    path('make-move', views.make_move)
]
