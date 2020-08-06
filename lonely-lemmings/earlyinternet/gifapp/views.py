import os

from django.shortcuts import render

CANVAS_DIR = os.path.join("editor", "base_draw.html")


def paint(request):
    return render(request, CANVAS_DIR)
