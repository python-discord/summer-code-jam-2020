from django.conf.urls import url, include
from .views import paint

urlpatterns = [
    url(r"^$", paint),
    #url(r"^files/", files, name="files"),
    #url("r^search/", search, name="search")
]

