from django.urls import path
from .views import RoverProfileView

urlpatterns = [
    path("rover/<slug:username>/", RoverProfileView.as_view(), name="rover-profile"),
    # path("rover/<int:pk>/", RoverProfileView.as_view(), name="rover-profile"),
]
