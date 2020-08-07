from django.urls import path
from . import views

urlpatterns = [
    path("", views.paint, name="paint"),
    path("save", views.parse_save_request, name="save"),
    path("back", views.return_home, name="back"),
    path("render", views.parse_render_request, name="render")
]
