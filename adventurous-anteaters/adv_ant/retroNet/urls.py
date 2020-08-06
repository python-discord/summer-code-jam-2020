from django.urls import path, include
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('post', views.createpost, name='post'),
    path('posted', views.index, name='index'),

]
