from django.urls import path

from . import views as myplace_views


urlpatterns = [
    path('home/', myplace_views.home),
    path('<int:username_or_id>/', myplace_views.user, name='user-profile'),
    path('<str:username_or_id>/', myplace_views.user, name='user-profile'),
    path('<str:username_or_id>/blog', myplace_views.blog, name='user-blog')
]
