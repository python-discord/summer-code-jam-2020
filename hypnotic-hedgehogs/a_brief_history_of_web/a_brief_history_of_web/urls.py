"""a_brief_history_of_web URL Configuration

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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='main-page'),
                  path('admin/', admin.site.urls),
                  path('web_portal', include('web_portal.urls', namespace='web_portal')),
                  path('ninetys_blog', include('ninetys_blog.urls', namespace='ninetys_blog')),
                  path('first_google', include('first_google.urls', namespace='first_google')),
                  path('first_twitter', include('first_twitter.urls', namespace='first_twitter')),
                  path('first_youtube', include('first_youtube.urls', namespace='first_youtube')),
                  path('win95', include('win95.urls', namespace='win95')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)