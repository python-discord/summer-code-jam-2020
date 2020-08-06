import os
import json
from base64 import b64decode
from PIL import Image as pilimage
from io import BytesIO
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from .models import *

CANVAS_DIR = os.path.join("editor", "base_draw.html")


def paint(request):
    return render(request, CANVAS_DIR)

@csrf_exempt
def parse_save_request(request):
    if request.method == "POST":
        data = json.loads(request.body)
        images_blob = data['image_BLOB']

        for i,blob in images_blob:
            im = pilimage.open(BytesIO(b64decode(blob.split(',')[1])))
            try:
                im.save(f"img/{request.user}_{i}.png")
            except FileNotFoundError:
                os.mkdir("img/")
                im.save(f"img/{request.user}_{i}.png")
        # project= Project.objects.get(data['project_id'])
        # Image.objects.add(project_id = project, image_name = )
    return redirect("/")

def parse_render_request(request):
    if request.method == "POST":
        pass # parse file byte data and save it
    # grab all files from the project and compile it into a gif
    # render "preview.html"
    # send gif over as byte as http response


class ProjectListView(ListView):

    model = Project
    paginate_by = 10
    ordering = ['-date_created']

    # TODO: Please replace template with something that isn't terrible
    template_name = 'project_feed/project_list.html'

