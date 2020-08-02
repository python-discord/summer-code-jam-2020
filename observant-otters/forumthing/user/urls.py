from django.urls import path, re_path
from . import views

urlpatterns = [
	re_path(
        r"^forum/messages/(?P<id>\d+)/$",
        views.message,
        name="message-action"
    )
]