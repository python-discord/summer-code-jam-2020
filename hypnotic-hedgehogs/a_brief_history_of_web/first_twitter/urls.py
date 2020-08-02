from django.urls import path
from . import views


app_name = 'first_twitter'

urlpatterns = [
    path('', views.index, name='index')
]