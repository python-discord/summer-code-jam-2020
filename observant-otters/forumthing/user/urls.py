from django.urls import path, re_path

from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    re_path(
        r"^forum/messages/(?P<id>\d+)/$",
        views.message,
        name="message-action"
    ),
]
