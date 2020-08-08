from django.urls import path

from . import views

urlpatterns = [
    path("", views.paint, name="paint"),
    path("", views.)
    path("save", views.parse_save_request, name="save"),
    path("back", views.return_home, name="back"),
    path("render", views.parse_render_request, name="render"),
    path("project/<str:project_name>", views.parse_image_request, name="images")
]
