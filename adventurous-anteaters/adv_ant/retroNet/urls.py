from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    re_path(r'^$', views.my_profile, name='profile_two'),
    path('post', views.createpost, name='post'),
    path('posted', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('updateprofile', views.update_profile, name='updateprofile'),
    path('updateprofiledisplay', views.update_profile_display,
         name='updateprofiledisplay'),
    path('profile', views.my_profile, name="my_profile"),
    path('logout', views.logout_page, name="logout_test"),
    path('logout_confirm', views.logout_request, name="logout_done"),
    path('account_deletion', views.account_deletion, name='account_deletion'),
    path('create_tweet', views.create_tweet, name="create_tweet"),
    path('view_tweet', views.view_tweet, name="view_tweet")
]
