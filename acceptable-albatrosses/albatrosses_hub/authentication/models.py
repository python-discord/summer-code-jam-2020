from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class HubUser(models.Model):
    """A Class model that will store user information."""

    email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=512)

    def __str__(self):
        # Will display user id on Django admin
        return self.username

    def process(self, form):
        """Function to store form data into django model."""

        self.email = form.cleaned_data["email"]
        self.username = form.cleaned_data["username"]
        self.password = make_password(form.cleaned_data["password"])
