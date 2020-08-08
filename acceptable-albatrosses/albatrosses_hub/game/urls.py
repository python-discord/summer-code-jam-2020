from django.urls import path, include
from .views import gamepage

urlpatterns = [
    path("", gamepage, name="gamepage")
]
