from django.urls import path
from .views import Welcome
from .views import Construction

app_name = "welcome_page"
urlpatterns = [
    path("", Welcome.as_view(), name="welcome_page"),
    path("test/", Construction.as_view(), name="under_construction"),
]
