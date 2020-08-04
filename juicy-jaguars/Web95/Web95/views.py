"""Functions for serving pages on the site."""

from django.shortcuts import render, redirect
from .settings import BASE_DIR
from random import choice
import os


def landing_page(request):
    """Landing Page view."""
    themes = os.listdir(os.path.join(BASE_DIR,
                                     "Web95/static/images/wallpapers"))

    try:
        if request.GET["theme"] in themes:
            theme = request.GET["theme"]
        else:
            theme = "Win95"
    except KeyError:
        theme = "Win95"

    wallpaper_path = os.path.join(BASE_DIR,
                                  "Web95/static/images/wallpapers/" + theme)

    bg = choice(os.listdir(wallpaper_path))

    themelist = []

    for n in themes:
        themelist.append("<li class=\"start-lvl3-item\"> <a href='?theme=" + n
                         + "'>" + n + "</n></li>")

    return render(request,
                  "Web95/landing_page.html",
                  {"bg": "url(\"static/images/wallpapers/" + theme + "/"
                   + bg + "\")",
                   "themes": "\n".join(themelist),
                   },
                  )


def index(request):
    """Redirect from index.html to /."""
    return redirect(landing_page)
