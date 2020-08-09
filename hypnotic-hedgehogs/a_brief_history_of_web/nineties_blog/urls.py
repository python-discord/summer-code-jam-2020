from django.urls import path, include
from . import views

app_name = 'nineties_blog'
urlpatterns = [
    path('', views.index, name='index')
    
]
