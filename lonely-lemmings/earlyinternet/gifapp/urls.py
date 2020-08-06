from django.conf.urls import url
from .views import paint, parse_save_request, ProjectListView

urlpatterns = [
    url(r"^$", paint),
    url(r"save/",parse_save_request),
    url(r"feed/$", ProjectListView.as_view())

]

