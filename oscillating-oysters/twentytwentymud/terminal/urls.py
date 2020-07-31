from django.urls import path


from . import views

urlpatterns = [
    path('', views.terminal, name='terminal'),
    path('command/<str:text>/', views.command, name='command'),
]
