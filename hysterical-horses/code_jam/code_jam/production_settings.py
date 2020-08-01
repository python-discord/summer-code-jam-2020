import os
from .settings import *

DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "db name",
        "USER": "user",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "port",
    }
}
