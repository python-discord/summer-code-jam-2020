from django.urls import path
from . import views

app_name = 'ninetys_blog'
urlpatterns = [
    path('', views.index, name='index')
]