"""Functions for serving pages on the site."""

from django.shortcuts import render, redirect  # Django utilities
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.http import HttpResponse, HttpResponseNotFound
import io  # For BytesIO
import os  # Various functions
import urllib.parse  # For parsing URLs with escape codes
import requests  # For fetching webpages
from math import floor  # For image resizing
from PIL import Image, UnidentifiedImageError  # For image processing
from .html_parse import HtmlParser  # Our HTML parser
from .settings import BASE_DIR  # For Base Directory path


def landing_page(request):
    """Serve the main page of the site.

    This fetches themes, wallpapers etc. and serves the neccessary elements to the webpage.
    """
    themes = os.listdir(os.path.join(BASE_DIR,
                                     "Web95/static/images/wallpapers"))

    try:
        if request.GET["theme"] in themes:  # Check that the theme in URL is valid
            theme = request.GET["theme"]  # Get theme from URL GET params
        else:
            theme = "Win95"  # If its not a valid theme, set to Win95
    except KeyError:
        theme = "Win95"  # If its not in the GET Params, set to Win95

    wallpapers = sorted(os.listdir(os.path.join(BASE_DIR,
                                                "Web95/static/images/wallpapers",
                                                theme)))  # Get the wallpaper list from directory.

    try:
        if request.GET["wallpaper"] in wallpapers:  # Check that the wallpaper in URL is valid
            wallpaper = request.GET["wallpaper"]  # Get wallpaper from URL GET params
        else:
            wallpaper = wallpapers[0]  # If wallpaper is not valid, set to the first in folder
    except KeyError:
        wallpaper = wallpapers[0]  # If wallpaper is not in URL, set to first in folder

    bg = "/static/images/wallpapers/" + theme + "/" + wallpaper  # Set BG path

    themelist = []  # List of theme Button elements
    walllist = []  # List of wallpaper Button elements

    for n in themes:
        # Add all theme buttons to list
        themelist.append("<li class=\"start-lvl3-item\"> <a href='?theme=" + n + "'>" + n + "</a></li>")

    for n in wallpapers:
        # Add all wallpaper buttons to list
        walllist.append(
            "<li class=\"start-lvl3-item\"> <a href='?theme=" + theme + "&wallpaper=" + n + "'>" + n + "</a></li>")

    return render(request,
                  "Web95/landing_page.html",
                  {"bg": "url('" + bg + "')",
                   "themes": "\n".join(themelist),
                   "wallpapers": "\n".join(walllist),
                   },
                  )  # Serve the webpage.
# BG puts the path to wallpaper in. Themes and wallpapers are buttons for the start menu


def index(request):
    """Redirect from index.html to /.

    If someone tries to visit /index.html, we want to redirect them to the proper path for the site index
    """
    return redirect(landing_page)


@xframe_options_sameorigin  # Ensure it can be served inside an iFrame
def page(request, url):  # Url is the URL we want to visit
    """Handle /page urls. Used to serve pages to IE.

    /page URLs are used to parse pages which will be served in Internet Explorer.
    It first checks if the URL is for an Easter egg, if not it will process it as a URL
    """
    print(url)
    if url == "1995":  # For 1995 Easter egg?
        content = "<img src='/static/images/404.gif' height='100%'>"
        return render(request, "Web95/blank.html", {"content": content})
    elif url == "Mother Russia":  # For Soviet Easter egg?
        content = "<img src='/static/images/mother-russia.jpg' height='100%'>"
        return render(request, "Web95/blank.html", {"content": content})
    else:  # Ensure that the URL has a scheme
        if not(url.startswith("http://") or url.startswith("https://")):
            url = "http://" + url

        url = urllib.parse.unquote(url)  # The URL is parsed on the page to ensure URL chars dont mess with it
        print("\u001b[32m" + url + "\u001b[0m")  # Log the URL we parsed.

        params = []  # URL Params. Sometimes these are parsed properly,
# so we need to hand them from our URL to the site

        for key, val in request.GET.items():  # Go through our GET params
            params.append(key + "=" + val)  # Process those GET params

        if len(params) > 0:  # If we have GET params to add, add them to the URL
            url += "?" + ("&".join(params))

        if request.method == "GET":  # If the HTTP method is GET, send a GET request to the target
            req = requests.get(url, params={'User-Agent': request.META["HTTP_USER_AGENT"]})  # Send request.
        elif request.method == "POST":  # If the HTTP method is POST, send a POST request to the target
            req = requests.post(url, data=request.POST, params={'User-Agent': request.META["HTTP_USER_AGENT"]})
# Send request with POST params

        if req.headers["content-type"].split("/")[0] in ["text", "application"]:
            # If we're processing a text file, then encode and process it as a text file
            content = req.text  # Our content is just what we recieve

            if req.headers["content-type"].split(";")[0] == "text/html":
                # If its a HTML doc, run it through our HTML parser
                parser = HtmlParser(content, url, request)
                parser.parse()

                content = "<!-- Yep, this got parsed! -->\n" + parser.soup.prettify()
                # Get our HTML from the parser, and put a comment on so we know the site was parsed.

            # Put our content into a HttpResponse for django and add the content type header
            resp = render(request, "Web95/blank.html", {"content": content})
            resp["content-type"] = req.headers["content-type"]

            return resp  # Return our reponse from the View function
        elif req.headers["content-type"].split("/")[0] == "image":
            # If we're processing an Image, treat it as an image.
            data = req.content  # We need to get the raw bytes as we're dealing with a file, not text

            stream = io.BytesIO(data)  # Create a Byte Stream that PIL can read

            # Create our HTTP response to write the image to
            response = HttpResponse(content_type=req.headers["content-type"])

            if "svg" in \
               req.headers["content-type"].split(";")[0].split("/")[1]:  # If we've got an SVG, treat it as text.
                # SVG files are actually XML, unlike normal images.
                img = req.text
                resp = render(request, "Web95/blank.html", {"content": img})
                resp["content-type"] = req.headers["content-type"]

            else:  # If its a normal image, we need to process it with PIL.
                try:
                    img = Image.open(stream)  # Open the bytes stream with PIL

                    # Get the file type from the HTTP headers
                    f_ext = req.headers["content-type"].split(";")[0].split("/")[1]
                    if f_ext.upper() == "VND.MICROSOFT.ICON":
                        # If its an ICO file, the HTTP type is not the same as the extension. So we need to change it.
                        # PNG Seems to work fine for this.
                        f_ext = "png"

                    resize_factor = 3  # Factor to pixellate the image
                    # Reduce image resolution
                    img = img.resize(list(map(lambda x: floor(x / resize_factor), img.size)), resample=Image.NEAREST)
                    # Scale image back up, but use NEAREST so it becomes blocky
                    img = img.resize(list(map(lambda x: floor(x * resize_factor), img.size)), resample=Image.NEAREST)
                    img.save(response, f_ext)  # Save image into our HttpResponse
                except UnidentifiedImageError:  # If PIL doesnt know what the image is,
                    # Log that the image loading failed.
                    print("\u001b[34mImage processing failed!. Type was", req.headers["content-type"], "\u001b[0m")
                    return HttpResponseNotFound()  # Return a 404 Not Found.

            return response  # Return our response to Django
        else:
            # We dont know the content type. Return a 404

            # Log that there was an unknown content type.
            print("\u001b[34mContent Type Unknown", req.headers["content-type"], "\u001b[0m")

            return HttpResponseNotFound()  # Return a 404 not found.
