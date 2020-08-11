from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="chat"),
    path("<str:room_name>/", views.room, name="room"),
    # This url path must be dependent on user ids(do not cascade/unchangeable
    # by the user), as users can cascade and usernames are changeable.
    path("<int:user_id>-<int:friend_id>", views.froom, name="froom")
    ]
