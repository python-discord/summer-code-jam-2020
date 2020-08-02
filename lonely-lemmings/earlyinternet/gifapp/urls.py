from django.conf.urls import url, include
from gifapp.views import dashboard

urlpatterns = [
    url(r"^$", edit, name="edit"),
    url(r"^files/", files, name="files"),
    url("r^search/", search, name="search")
]

