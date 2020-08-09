from django.urls import path

from . import views

urlpatterns = [
    path('new_news', views.get_new_newsfeed, name='get_new_newsfeed'),
    path('best_news', views.get_best_newsfeed, name='get_best_newsfeed'),
]

# , name='get_new_newsfeed'
# , name='get_best_newsfeed'
