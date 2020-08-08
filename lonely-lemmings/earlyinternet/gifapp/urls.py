from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from . import userviews

urlpatterns = [
    path("", views.paint, name="paint"),
    path("save", views.parse_save_request, name="save"),
    path("back", views.return_home, name="back"),
    path("project/<str:project_name>/render", views.parse_render_request, name="render"),
    path("project/<str:project_name>/post", views.parse_image_request, name="images"),
    path("project/<str:project_name>", views.parse_image_request, name="images"),

    path("about", userviews.about, name="about"),

    # template is project_form.html
    path("project/new/",
         userviews.ProjectCreateView.as_view(template_name="project_form.html"),
         name="project-create"),
    # template is project_detail.html
    path("project/<int:pk>/",
         userviews.ProjectDetailView.as_view(template_name="project_detail.html"),
         name="project-detail"),
    # template is project_confirm_delete.html
    path("project/<int:pk>/delete",
         userviews.ProjectDeleteView.as_view(template_name="project_confirm_delete.html"), name="project-delete"),
    # template is project_detail.html
    path("project/<int:pk>/update", userviews.ProjectUpdateView.as_view(), name="project-update"),

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
