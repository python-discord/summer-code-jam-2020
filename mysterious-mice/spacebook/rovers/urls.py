from django.urls import path
from .views import RoverProfileView, RoverProfileListView

app_name = "rovers"
urlpatterns = [
    path("rover/<slug:username>/", RoverProfileView.as_view(), name="rover-profile"),
    path("rover/", RoverProfileListView.as_view(), name="rover-list"),
]
