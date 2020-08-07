import os
import json
from typing import Union

from base64 import b64decode
from PIL import Image as PILImage
from io import BytesIO
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Project, Image

APP_DIR = os.path.join(settings.BASE_DIR, "gifapp")
MEDIA_DIR = os.path.join(APP_DIR, "media")

CANVAS_DIR = os.path.join("editor", "base_draw.html")


def paint(request) -> HttpResponse:
    return render(request, CANVAS_DIR)


@csrf_exempt
def parse_save_request(request) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect]:
    """receives POST request of images as bytes, decodes and saves image paths to database"""

    if request.method == "POST":
        data = json.loads(request.body)
        images_blob = data['image_BLOB']
        project_name = data['name']

        # since project name is distinct for each user, there can only be one
        project = Project.objects.filter(name=project_name, user_id=request.user)[0]

        # check if there are previous images, if so delete all images associated with the project
        images = Image.objects.filter(project_id=project)
        print(images)
        if len(images) > 0:
            images.delete()

        # write request images to file and associate them with project
        for i, blob in enumerate(images_blob):
            im = PILImage.open(BytesIO(b64decode(blob.split(',')[1])))
            image_name = f"{request.user}_{project_name}_{i}.png"
            image_dir = os.path.join(MEDIA_DIR, image_name)
            im.save(image_dir)
            Image.objects.create(project_id=project, image_data=image_name, animation_position=i)
    return redirect("/")


@csrf_exempt
def parse_render_request(request):
    if request.method == "POST":
        pass  # parse file byte data and save it
    # grab all files from the project and compile it into a gif
    # render "preview.html"
    # send gif over as byte as http response
