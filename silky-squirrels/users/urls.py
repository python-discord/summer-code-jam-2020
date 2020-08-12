from django.urls import path
from .views import send_request, accept_request

urlpatterns = [
    path("add-friend/<int:id>/", send_request, name="add-friend"),
    path("accept/<int:id>/", accept_request, name="accept"),
]
