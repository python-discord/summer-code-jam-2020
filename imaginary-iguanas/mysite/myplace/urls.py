from django.urls import path

from . import views as myplace_views


urlpatterns = [
    path('<int:user_id>/', myplace_views.user, name='user-id'),
]
