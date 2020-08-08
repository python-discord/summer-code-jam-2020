from django.urls import path, include
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('post', views.createpost, name='post'),
    path('posted', views.index, name='index'),
    path('home', views.home, name='home'),
    path('updateprofile', views.update_profile, name='updateprofile'),
    path('updateprofiledisplay', views.update_profile_display, name='updateprofiledisplay'),
    path('profile', views.my_profile, name="my_profile")
]
