from django.urls import path
from . import views


urlpatterns = [
    path('<int:PostId>/', views.post, name='viewpost'),
    path('', views.index, name='home')
]
