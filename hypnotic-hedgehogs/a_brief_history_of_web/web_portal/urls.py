from django.urls import path
from . import views

app_name = 'web_portal'
urlpatterns = [
    path('', views.index, name='index')
]