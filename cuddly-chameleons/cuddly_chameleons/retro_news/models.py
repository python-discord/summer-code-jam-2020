from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Extend default user for case when we need to add something to this."""

    pass
