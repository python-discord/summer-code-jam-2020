import os

from django.shortcuts import render

CANVAS_DIR = os.path.join("editor", "draw.html")


def paint(request):
    return render(request, CANVAS_DIR)
