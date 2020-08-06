from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path(
        "forum/messages/<int:id>",
        views.message,
        name="message-action"
    ),
]
