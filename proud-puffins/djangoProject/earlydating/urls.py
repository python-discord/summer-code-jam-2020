from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='earlydating-home'),
    path('about/', views.about, name='earlydating-about'),
]
