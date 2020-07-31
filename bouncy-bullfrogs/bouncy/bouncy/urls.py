from django.contrib import admin
from mail import views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path('', include('mail.urls'))
]
