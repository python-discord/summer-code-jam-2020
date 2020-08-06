import os

from django.shortcuts import render

CANVAS_DIR = os.path.join("editor", "base_draw.html")


def paint(request):
    return render(request, CANVAS_DIR)


def parse_save_request(request):
    if request.method == "POST":
        pass  # parse file byte data and save it
    # check if json a next frame wants to be made


def parse_render_request(request):
    if request.method == "POST":
        pass # parse file byte data and save it
    # grab all files from the project and compile it into a gif
    # render "preview.html"
    # send gif over as byte as http response
