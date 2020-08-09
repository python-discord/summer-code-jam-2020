from django.urls import include, path

urlpatterns = [
    path("posts/", include("posts.urls")),
    path("users/", include("users.urls")),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
]
