from django.conf.urls import url
from .views import paint, gallery
from .userviews import register, home, login

urlpatterns = [
    url(r"^$", home, name='feed-home'),
    url(r"^register/", register, name='feed-register'),
    url(r"^gallery/", gallery, name='feed-gallery'),
    url(r"^login/", login, name='feed-login'),
    url(r"^paint/", paint, name='draw-home'),
    #url(r"^files/", files, name="files"),
    #url("r^search/", search, name="search")
]

