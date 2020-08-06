from django.urls import path
from prompt import views

urlpatterns = [
    path('mud/', views.room, name='room'),
]
