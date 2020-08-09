"""lammas URL Configuration

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
from django.urls import path, re_path
from django.conf.urls.static import static
from lammas.settings import STATIC_URL, STATIC_ROOT
from django.conf.urls import include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', core_views.login_endpoint),
    path('api/logout', core_views.logout_endpoint),
    path('api/register', core_views.register_endpoint),
    path('api/chat/', include('chat.urls')),
    path('api/games/', include('games.urls')),
    path('api/forum/', include('forum.urls')),
    path('api/mail/', include('mailmessages.urls')),
    path('api/newsfeed/', include('newsfeed.urls'))
] + static(STATIC_URL, document_root=STATIC_ROOT) + [

    re_path(r'^.*$', core_views.index, name='unmatched'),
]
