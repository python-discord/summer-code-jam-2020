from django.urls import path

from shiny_sheep.games.api.views import RoomCreateView, RoomView

urlpatterns = [
    path('', RoomCreateView.as_view()),
    path('<int:game_id>/', RoomView.as_view()),
]
