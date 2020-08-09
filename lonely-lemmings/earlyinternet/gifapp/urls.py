from django.urls import path

from . import views

urlpatterns = [
    path("project", views.render_all_projects, name="projects"),
    path("project/create", views.parse_new_project_request, name="new"),
    path("project/<str:project_name>", views.paint, name="paint"),
    path("project/<str:project_name>/save", views.parse_save_request, name="save"),
    path("project/<str:project_name>/render", views.parse_render_request, name="render"),
    path("project/<str:project_name>/view", views.parse_view_request, name="view"),
    path("project/<str:project_name>/publish", views.parse_post_request, name="publish"),
    path("project/<str:project_name>/load", views.parse_image_request, name="images"),
]
