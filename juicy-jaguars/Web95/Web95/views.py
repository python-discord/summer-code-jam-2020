"""Functions for serving pages on the site."""

from django.shortcuts import render, redirect
from .settings import BASE_DIR
from random import choice
import os


def landing_page(request):
    """Landing Page view."""
    theme = "Win95"

    wallpaper_path = os.path.join(BASE_DIR,
                                  "Web95/static/images/wallpapers/" + theme)

    bg = choice(os.listdir(wallpaper_path))

    return render(request,
                  "Web95/landing_page.html",
                  {"bg": "url(\"static/images/wallpapers/" + theme + "/"
                   + bg + "\")",
                   },
                  )


def index(request):
    """Redirect from index.html to /."""
    return redirect(landing_page)
