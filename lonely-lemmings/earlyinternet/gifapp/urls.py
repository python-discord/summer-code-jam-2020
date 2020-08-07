from django.conf.urls import url
from .views import paint, parse_save_request, parse_render_request

urlpatterns = [
    url(r"^$", paint),
    url(r"save/", parse_save_request),
    url(r"back/", parse_save_request),
    url(r"render/", parse_render_request)
]
