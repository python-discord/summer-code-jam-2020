from django.urls import path
from . import views
app_name = 'mail'

urlpatterns = [
    path("", views.home, name="index"),
    path("home", views.home, name="home"),
    path("inbox", views.home, name="inbox"),
    path("home/inbox", views.home, name="inbox"),
    path("aboutus", views.info, name="aboutus"),
    # API Routes
    path("emails", views.compose, name="compose"),
    path("emails/<int:email_id>", views.email, name="email"),
    path("emails/<str:mailbox>", views.mailbox, name="mailbox"),
]
