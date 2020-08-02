from django.urls import path
from .views import RoverProfileView

app_name = "rovers"
urlpatterns = [
    path("rover/<slug:username>/", RoverProfileView.as_view(), name="rover-profile"),
    # path("rover/<int:pk>/", RoverProfileView.as_view(), name="rover-profile"),
]
