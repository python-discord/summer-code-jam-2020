"""Functions for serving pages on the site."""

from django.shortcuts import render, redirect
from .settings import BASE_DIR
import os
import urllib.parse
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.http import HttpResponse, HttpResponseNotFound
from .html_parse import HtmlParser
from PIL import Image, UnidentifiedImageError
import io
import requests
from math import floor


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
                         + "'>" + n + "</a></li>")
    print(themelist)

    for n in wallpapers:
        walllist.append("<li class=\"start-lvl3-item\"> <a href='?theme=" +
                        theme + "&wallpaper=" + n + "'>" + n + "</a></li>")
    print(walllist)

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
    print(url)
    if url == "1995":
        content = "<img src='/static/images/404.gif' height='100%'>"
        return render(request, "Web95/blank.html", {"content": content})
    elif url == "Mother Russia":
        content = "<img src='/static/images/mother-russia.jpg' height='100%'>"
        return render(request, "Web95/blank.html", {"content": content})
    else:
        if not(url.startswith("http://")
               or url.startswith("https://")):
            url = "http://" + url

        url = urllib.parse.unquote(url)
        print("\u001b[32m"+url+"\u001b[0m")

        params = []
        for key, val in request.GET.items():
            params.append(key+"="+val)

        if len(params) > 0:
            url += "?"+("&".join(params))

        if request.method == "GET":
            req = requests.get(url, params={'User-Agent': request.META["HTTP_USER_AGENT"]})
        elif request.method == "POST":
            req = requests.post(url, data=request.POST, params={'User-Agent': request.META["HTTP_USER_AGENT"]})

        if req.headers["content-type"].split("/")[0] in ["text", "application"]:
            content = req.text

            if req.headers["content-type"].split(";")[0] == "text/html":
                parser = HtmlParser(content, url, request)
                parser.parse()

                content = "<!-- Yep, this got parsed! -->\n" + parser.soup.prettify()

            resp = render(request, "Web95/blank.html", {"content": content})
            resp["content-type"] = req.headers["content-type"]

            return resp
        elif req.headers["content-type"].split("/")[0] == "image":
            data = req.content

            stream = io.BytesIO(data)

            response = HttpResponse(content_type=req.headers["content-type"])

            if "svg" in \
               req.headers["content-type"].split(";")[0].split("/")[1]:
                img = req.text
                resp = render(request, "Web95/blank.html", {"content": img})
                resp["content-type"] = req.headers["content-type"]

            else:
                try:
                    img = Image.open(stream)

                    f_ext = \
                        req.headers["content-type"].split(";")[0].split("/")[1]
                    if f_ext.upper() == "VND.MICROSOFT.ICON":
                        f_ext = "png"

                    resize_factor = 3
                    img = img.resize(list(map(lambda x: floor(x/resize_factor), img.size)), resample=Image.NEAREST)
                    img = img.resize(list(map(lambda x: floor(x*resize_factor), img.size)), resample=Image.NEAREST)
                    img.save(response, f_ext)
                except UnidentifiedImageError:
                    print("\u001b[34mImage processing failed!. Type was", req.headers["content-type"], "\u001b[0m")
                    return HttpResponseNotFound()

            return response
        else:
            print("\u001b[34mManual 404 oopsie. Type was",
                  req.headers["content-type"],
                  "\u001b[0m")

            return HttpResponseNotFound()
