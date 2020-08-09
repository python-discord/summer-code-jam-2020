"""sparrow_django URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

""" urls should always end with "/", see example at https://docs.djangoproject.com/en/3.0/topics/http/urls/ """
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="start.html"), name="home"),
    path("main", TemplateView.as_view(template_name="mainapp.html"), name="main"),
    path(
        "market", TemplateView.as_view(template_name="marketplace.html"), name="market"
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("stock/", include("sparrow_django.public.urls")),
]

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
