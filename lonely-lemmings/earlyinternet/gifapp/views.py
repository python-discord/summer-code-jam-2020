from base64 import b64decode, b64encode
from io import BytesIO
import json
import os
from typing import Union

from PIL import Image as PILImage
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Project, Image

APP_DIR = os.path.join(settings.BASE_DIR, "gifapp")
MEDIA_DIR = os.path.join(APP_DIR, "media")

CANVAS_DIR = os.path.join("editor", "base_draw.html")
PREVIEW_DIR = os.path.join("editor", "preview.html")


def paint(request) -> HttpResponse:
    return render(request, CANVAS_DIR)


@csrf_exempt
def parse_save_request(request) -> Union[HttpResponseRedirect, HttpResponsePermanentRedirect]:
    """receives POST request of images as bytes, decodes and saves image paths to database"""

    if request.method == "POST":
        data = json.loads(request.body)
        images_blob = data['image_BLOB']
        project_name = data['name']

        # get project id
        project = Project.objects.filter(name=project_name, user_id=request.user)[0]

        # delete all images associated with project
        images = Image.objects.filter(project_id=project)
        image_path_list = [get_img_path(img) for img in images]
        images.delete()

        # delete all local images associated with the project
        if image_path_list:
            for img_path in image_path_list:
                os.remove(img_path)

        # write request images to file and associate them with project
        for i, blob in enumerate(images_blob):
            im = PILImage.open(BytesIO(b64decode(blob.split(',')[1])))
            image_name = f"{request.user}_{project_name}_{i}.png"
            image_dir = os.path.join(MEDIA_DIR, image_name)
            im.save(image_dir)
            Image.objects.create(project_id=project, image_data=image_name, animation_position=i)
    return redirect("/")


def get_img_path(image: Image) -> str:
    """returns the path of the image given an image"""
    img_name = image.image_data.url.split("/")[2]
    return os.path.join(MEDIA_DIR, img_name)


def parse_render_request(request, project_name=None):
    """receives GET request with project_name.
    Grab all files from the project with name project_name and compile it into a gif in the media folder
    with name <user_name>_<project_name>.gif render preview.html with the gif img loaded"""
    images = Image.objects.filter(project_id__name=project_name, project_id__user_id=request.user)
    if len(images) > 1:
        image_list = [get_img_path(img) for img in images]
        gif_path = os.path.join(MEDIA_DIR, f"{request.user}_{project_name}.gif")

        images_for_gif_compile = [PILImage.open(img) for img in image_list]

        # save the frames
        images_for_gif_compile[0].save(gif_path, save_all=True, append_images=images_for_gif_compile[1:],
                                       duration=100, loop=0)

        context = {
            "name": project_name
        }
        return render(request, PREVIEW_DIR, context)
    else:
        return HttpResponseNotFound()


def parse_image_request(request, project_name=None) -> HttpResponse:
    """ receives GET request with url with <project_name>,
    sends a JSON of ["data": <ordered list of images>]"""

    def encode_serializable_img(image) -> str:
        """encode image as base64 and remove the beginning 'b'"""
        img_path = get_img_path(image)
        with open(img_path, "rb") as image:
            return b64encode(image.read()).decode("utf-8")

    if request.method == "GET":

        images = Image.objects.filter(project_id__name=project_name, project_id__user_id=request.user)

        if images:
            image_data_list = [encode_serializable_img(img) for img in images]
        else:
            image_data_list = []
        data_dict = {"data": image_data_list}
        return HttpResponse(json.dumps(data_dict), content_type="application/json")
