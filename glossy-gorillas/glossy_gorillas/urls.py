"""glossy_gorillas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views
from django.urls import reverse_lazy

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("listings/", views.ListingList.as_view(), name="listings"),
    path("admin/", admin.site.urls),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="core/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page=reverse_lazy("home")),
        name="logout",
    ),
    path("dashboard/", views.TraderDashboard.as_view(), name="dashboard"),
    path("review/", views.ReviewCreateView.as_view(), name="review"),
    path(
        "inventory/create",
        views.InventoryAdditionForm.as_view(),
        name="inventory-create",
    ),
]
