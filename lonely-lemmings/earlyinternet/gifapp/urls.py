from django.urls import path
from django.contrib.auth import views as auth_views

from . import editorviews
from . import userviews

urlpatterns = [
    path("project", editorviews.render_all_projects, name="projects"),
    #path("project/create", editorviews.parse_new_project_request, name="new"),
    path("project/<str:project_name>", editorviews.paint, name="paint"),
    path("project/<str:project_name>/save", editorviews.parse_save_request, name="save"),
    path("project/<str:project_name>/render", editorviews.parse_render_request, name="render"),
    path("project/<str:project_name>/view", editorviews.parse_view_request, name="view"),
    path("project/<str:project_name>/publish", editorviews.parse_post_request, name="publish"),
    path("project/<str:project_name>/load", editorviews.parse_image_request, name="images"),


    path("feed/", userviews.home, name="home"),
    path("about/", userviews.about, name="about"),

    # template is project_form.html
    path("feedproject/new/", userviews.create, name="project-create"),
    # template is project_detail.html
    path("feedproject/<int:pk>/",
         userviews.ProjectDetailView.as_view(template_name="project_detail.html"),
         name="project-detail"),
    # template is project_confirm_delete.html
    path("feedproject/<int:pk>/delete/",
         userviews.ProjectDeleteView.as_view(template_name="project_confirm_delete.html"), name="project-delete"),
    # template is project_detail.html
    path("feedproject/<int:pk>/update/", userviews.ProjectUpdateView.as_view(), name="project-update"),

    # user authentication paths
    path("profile/", userviews.profile, name="profile"),
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
