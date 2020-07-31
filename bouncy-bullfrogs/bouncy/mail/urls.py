from django.urls import path
from . import views
app_name = 'mail'

urlpatterns = [
    path("home/", views.home, name="home"),
    # API Routes
    path("emails", views.compose, name="compose"),
    path("emails/<int:email_id>", views.email, name="email"),
    path("emails/<str:mailbox>", views.mailbox, name="mailbox"),
]
