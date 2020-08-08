from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.all_rooms, name="rooms"),
    path('rooms/create/', views.create_room, name="create_room"),
    # path('<str:room_name>/', views.room, name="room"),
    path('<int:room_id>/', views.room, name="room"),
]
