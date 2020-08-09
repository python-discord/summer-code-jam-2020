from django.urls import path
from . import views
from django.urls import re_path


urlpatterns = [
    path("", views.homepage),
    path("page/home", views.homepage),
    re_path("page/" + r"(?P<page_name>[a-zA-Z0-9]+)$", views.load_generated_page, name="load_generated_page"),
]
