"""Functions for serving pages on the site."""

from django.shortcuts import render, redirect
from .settings import BASE_DIR
import os
import urllib.parse
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.http import HttpResponse, HttpResponseNotFound
from .html_parse import HtmlParser
from PIL import Image
import io
import requests


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

        url = urllib.parse.unquote(url)
        print("\u001b[32m"+url+"\u001b[0m")

        params = []
        for key, val in request.GET.items():
            params.append(key+"="+val)

        url += "?"+("&".join(params))
        print(params)

        if request.method == "GET":
            req = requests.get(url,
                               params={'User-Agent':
                                       request.META["HTTP_USER_AGENT"]})
        elif request.method == "POST":
            print(request.POST)
            req = requests.post(url,
                                data=request.POST,
                                params={'User-Agent':
                                        request.META["HTTP_USER_AGENT"]})

        try:
            content = req.text

            parser = HtmlParser(content, url, request)
            parser.parse()

            content = "<!-- Yep, this got parsed! -->\n"+parser.soup.prettify()

            return render(request, "Web95/blank.html", {"content": content})
        except UnicodeDecodeError:
            data = req.content

            stream = io.BytesIO(data)

            img = Image.open(stream)

            response = HttpResponse(content_type="image/png")
            img.save(response, "PNG")

            return response
