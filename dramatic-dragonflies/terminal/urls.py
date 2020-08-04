from django.urls import path
from . import views
urlpatterns = [
    path("/<int:storage_id>/<int:pk>", views.index, name="index")
]
