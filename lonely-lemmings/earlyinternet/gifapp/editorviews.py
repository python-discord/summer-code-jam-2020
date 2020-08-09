from base64 import b64decode, b64encode
from io import BytesIO
import json
import os
from typing import Union

from PIL import Image as PILImage
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import ProjectForm
from .models import Project, Image

MEDIA_DIR = settings.MEDIA_ROOT


@login_required
def paint(request, project_name=None) -> HttpResponse:
    context = {
        "name": project_name
    }
    return render(request, "base_draw.html", context)


@login_required
@csrf_exempt
def parse_save_request(request, project_name=None) -> HttpResponse:
    """receives POST request of images as bytes, decodes and saves image paths to database"""

    data = json.loads(request.body)
    images_blob = data['image_BLOB']

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
        # fill transparent background with solid white
        white_bg = PILImage.new("RGBA", im.size, "WHITE")
        white_bg.paste(im, (0, 0), im)
        image_name = f"{request.user}_{project_name}_{i}.png"
        image_dir = os.path.join(MEDIA_DIR, image_name)
        white_bg.save(image_dir)
        Image.objects.create(project_id=project, image_data=image_name, animation_position=i)
    return HttpResponse("Saved")


def get_img_path(image: Image) -> str:
    """returns the path of the image given an image"""
    img_name = image.image_data.url.split("/")[2]
    return os.path.join(MEDIA_DIR, img_name)


@login_required
@csrf_exempt
def parse_render_request(request, project_name=None) -> Union[HttpResponse, HttpResponseNotFound]:
    """receives GET request with project_name.
    Grab all files from the project with name project_name and compile it into a gif in the media folder
    with name <user_name>_<project_name>.gif render preview.html with the gif img loaded"""
    project = Project.objects.filter(name=project_name, user_id=request.user)[0]
    images = Image.objects.filter(project_id=project)

    if len(images) > 1:
        image_list = [get_img_path(img) for img in images]
        gif_name = f"{request.user}_{project_name}.gif"
        gif_path = os.path.join(MEDIA_DIR, gif_name)
        images_for_gif_compile = [PILImage.open(img) for img in image_list]
        # save the frames
        images_for_gif_compile[0].save(gif_path, save_all=True, append_images=images_for_gif_compile[1:],
                                       duration=100, loop=0)
        # add a preview version to project
        project.preview_version = gif_name
        project.save()
        return HttpResponse("Build Successful")
    else:
        return HttpResponseNotFound("Cannot Find Enough Frames")


@login_required
def parse_image_request(request, project_name=None) -> HttpResponse:
    """ receives GET request with url with <project_name>,
    sends a JSON of ["data": <ordered list of images>]"""

    def encode_serializable_img(image) -> str:
        """encode image as base64 and remove the beginning 'b'"""
        img_path = get_img_path(image)
        with open(img_path, "rb") as image:
            return b64encode(image.read()).decode("utf-8")

    images = Image.objects.filter(project_id__name=project_name, project_id__user_id=request.user)

    if images:
        image_data_list = [encode_serializable_img(img) for img in images]
    else:
        image_data_list = []
    data_dict = {"data": image_data_list}
    return HttpResponse(json.dumps(data_dict), content_type="application/json")


@login_required
def parse_post_request(request, project_name=None):
    project = Project.objects.filter(name=project_name, user_id=request.user)[0]
    project.upload_version = project.preview_version
    project.save()
    return redirect("home")


@login_required
def parse_view_request(request, project_name=None):
    """displays a page that shows the built gif"""
    project = Project.objects.filter(name=project_name, user_id=request.user)[0]
    context = {
        "title": project.name,
        "path": project.preview_version.url
    }
    return render(request, "preview.html", context)


@login_required
def render_all_projects(request) -> HttpResponse:
    """displays all projects by the user"""
    projects = Project.objects.filter(user_id=request.user)
    return render(request, "view_projects.html", {"projects": projects, "form": ProjectForm()})


@login_required
def parse_new_project_request(request) -> HttpResponseRedirect:
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project_name = form.cleaned_data["project_name"]
            Project.objects.create(name=project_name, user_id=request.user)
            return HttpResponseRedirect(f"/project/{project_name}")
        else:
            return HttpResponseRedirect("../project")

    else:
        return HttpResponseRedirect("../project")
