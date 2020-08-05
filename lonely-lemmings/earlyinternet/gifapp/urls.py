from django.conf.urls import url
from .views import paint

urlpatterns = [
    url(r"^$", paint),
]

