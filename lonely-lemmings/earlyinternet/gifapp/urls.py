from django.urls import path
from django.contrib.auth import views as auth_views

from . import editorviews
from . import userviews

urlpatterns = [
    # editor paths
    path("project", editorviews.render_all_projects, name="projects"),
    path("project/create", editorviews.parse_new_project_request, name="new"),
    path("project/<str:project_name>", editorviews.paint, name="paint"),
    path("project/<str:project_name>/save", editorviews.parse_save_request, name="save"),
    path("project/<str:project_name>/render", editorviews.parse_render_request, name="render"),
    path("project/<str:project_name>/view", editorviews.parse_view_request, name="view"),
    path("project/<str:project_name>/publish", editorviews.parse_post_request, name="publish"),
    path("project/<str:project_name>/load", editorviews.parse_image_request, name="images"),
    path("project/<str:user>/<str:project_name>/detail", userviews.detail, name="project-detail"),
    path("project/<str:user>/<str:project_name>/comment", userviews.submit_comment, name="submit-comment"),

    path("", userviews.home, name="home"),

    # user authentication paths
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path("register/", userviews.register, name="register"),

    # password reset paths
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path("password_reset/done", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path("password_reset/confirm",
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path("password_reset/complete",
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]
