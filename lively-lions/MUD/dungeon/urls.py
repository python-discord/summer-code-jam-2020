from django.urls import path, re_path
from .views import example_view
from .views import frontend_view
from .views.mud_user_account import MudUserView
from .views.character_view import CharacterView


##
# matters that require attention
# Get method  - localhost:8000/api/example/ (o)
#             - localhost:8000/api/example  (maybe o)
# Post method - localhost:8000/api/example/ (o)
#             - localhost:8000/api/example/ (x) (I checked that it didn't work.)
##
urlpatterns = [
    path('api/example/', example_view.rest),
    re_path(r'api/example/[0-9a-zA-Z]', example_view.rest),
    path('', frontend_view.index, name='index'),
    path('api/muduser/', MudUserView.as_view()),
    path('api/character/', CharacterView.as_view()),
]
