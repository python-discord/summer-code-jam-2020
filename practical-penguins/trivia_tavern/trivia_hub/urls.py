from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_hub, name='main_hub'),
]
