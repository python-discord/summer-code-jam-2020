from django.urls import path
from . import views

urlpatterns = [
    path("", views.default, name="userwall"),
    path("<str:profile_name>/", views.wall, name="wall1"),
    # Test website
    # path("potato", views.default, name="wall2"),
]
