from django.urls import path

from shiny_sheep.chat.api.views import RoomCreateView, RoomView

urlpatterns = [
    path('', RoomCreateView.as_view()),
    path('/<int:pk>/', RoomView.as_view()),
]
