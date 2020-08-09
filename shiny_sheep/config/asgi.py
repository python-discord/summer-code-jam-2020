"""
ASGI config for Shiny Sheep project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/

"""
import os
import sys
from pathlib import Path

from channels.routing import get_default_application
import django

# This allows easy placement of apps within the interior
# shiny_sheep directory.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "shiny_sheep"))

# If DJANGO_SETTINGS_MODULE is unset, default to the local settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

django.setup()

# This application object is used by any ASGI server configured to use this file.
django_application = get_default_application()

# Apply ASGI middleware here.
# from helloworld.asgi import HelloWorldApplication
# application = HelloWorldApplication(application)

# Import websocket application here, so apps from django_application are loaded first
# from config.websocket import websocket_application  # noqa isort:skip

application = django_application
