import os

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("db_name"),
        "USER": os.environ.get("db_user"),
        "PASSWORD": os.environ.get("db_password"),
        "HOST": os.environ.get("db_host"),
        "PORT": os.environ.get("db_port"),
    }
}
