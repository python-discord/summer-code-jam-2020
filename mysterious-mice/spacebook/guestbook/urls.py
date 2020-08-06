from django.urls import path
from .views import Guestbook

app_name = "guestbook"
urlpatterns = [
    path("guestbook/", Guestbook.as_view(), name="guestbook"),
]
