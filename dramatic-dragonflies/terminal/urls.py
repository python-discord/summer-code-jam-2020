from django.urls import path
from . import views
urlpatterns = [
    path("call/<str:storage_id>/<int:vm_id>", views.index, name="index"),
    path("test", views.test),
]
