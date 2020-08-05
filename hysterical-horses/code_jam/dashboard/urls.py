from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard-index'),
    path('results/<str:search_text>', views.engine_results, name="engine-results"),
    path('chat/<str:room_name>/', views.chat_room, name="chat-room"),
]
