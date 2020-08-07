from django.urls import path, re_path

from .views import example_view

# #
# prefix : api/
# example : localhost:8080/api/example
urlpatterns = [
    path('example/', example_view.rest),
    re_path(r'example/[0-9a-zA-Z]', example_view.rest),
]
