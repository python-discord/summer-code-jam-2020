"""Functions for serving pages on the site."""

from django.shortcuts import render, redirect
from .settings import BASE_DIR
import os
import urllib.parse
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .html_parse import HtmlParser


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

    wallpapers = sorted(os.listdir(os.path.join(BASE_DIR,
                                                "Web95/static/images/\
wallpapers",
                                                theme)))

    try:
        if request.GET["wallpaper"] in wallpapers:
            wallpaper = request.GET["wallpaper"]
        else:
            wallpaper = wallpapers[0]
    except KeyError:
        wallpaper = wallpapers[0]

    bg = "/static/images/wallpapers/" + theme + "/" + wallpaper

    themelist = []
    walllist = []

    for n in themes:
        themelist.append("<li class=\"start-lvl3-item\"> <a href='?theme=" + n
                         + "'>" + n + "</n></li>")

    for n in wallpapers:
        walllist.append("<li class=\"start-lvl3-item\"> <a href='?theme=" +
                        theme + "&wallpaper=" + n + "'>" + n + "</n></li>")

    return render(request,
                  "Web95/landing_page.html",
                  {"bg": "url('" + bg + "')",
                   "themes": "\n".join(themelist),
                   "wallpapers": "\n".join(walllist),
                   },
                  )


def index(request):
    """Redirect from index.html to /."""
    return redirect(landing_page)


@xframe_options_sameorigin
def page(request, url):
    """Handle /page urls. Used to serve pages to IE."""
    if url == "1995":
        content = "<img src='/static/images/404.gif' height='100%'>"
    else:
        if not(url.startswith("http://")
               or url.startswith("https://")):
            url = "http://" + url

        req = urllib.request.Request(url,
                                     headers={'User-Agent':
                                              request.META["HTTP_USER_AGENT"]})
        fp = urllib.request.urlopen(req)
        content = fp.read().decode()

        parser = HtmlParser(content, url)
        parser.parse()

        content = parser.soup.prettify()

    return render(request, "Web95/blank.html", {"content": content})
