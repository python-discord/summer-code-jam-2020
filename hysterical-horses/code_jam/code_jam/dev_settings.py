# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

import os
from .settings import BASE_DIR

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}
