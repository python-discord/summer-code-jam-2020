from django.urls import path

from . import views

urlpatterns = [
    path("", views.paint, name="paint"),
    path("save", views.parse_save_request, name="save"),
    path("project/<str:project_name>/render", views.parse_render_request, name="render"),
    path("project/<str:project_name>/post", views.parse_image_request, name="images"),
    path("project/<str:project_name>", views.parse_image_request, name="images"),
]
