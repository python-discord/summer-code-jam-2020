from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import TodoEntryCreate


urlpatterns = [
    path('/add', login_required(TodoEntryCreate.as_view()), name='todo-create')
]