import hashlib
import os
import random

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

from .models import File


def index(request):
    return HttpResponse("welcome")


def show_diff():
    pass


def hash_file(filename):
    """"This function returns the SHA-1 hash
    of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()
    with open(filename, "rb") as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b"":
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


def check_title_presence(uploaded_file):
    """
    query database for filename and if it is present then return True else False
    """
    file = File.objects.filter(title=uploaded_file)
    if file:
        return True
    return False


def check_file_presence(hash_val):
    """

    """
    file = File.objects.filter(hash_val=hash_val)
    if file:
        return True
    return False


def save_on_server(uploaded_file):
    """

    """
    fs = FileSystemStorage()
    name = fs.save(uploaded_file.name, uploaded_file)
    url = fs.url(name)
    path = "/".join(os.path.dirname(os.path.realpath(__file__)).split("/")[:-1])
    return path + url


def upload(request):
    """

    """
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES["document"]
        if not check_title_presence(uploaded_file):
            messages.success(request, "New file save successfully.")
            path = save_on_server(uploaded_file)
            hash_val = hash_file(path)
            form = File(title=uploaded_file.name, hash_val=hash_val)
            form.save()
        else:
            # flash message that A similar file is already present  if hash value matches

            path = save_on_server(uploaded_file)
            hash_val = hash_file(path)
            if check_file_presence(hash_val):
                messages.warning(request, "A similar file is already present")
                os.remove(path)

            # hash value matches so no need to upload. if not uploade it with different file name
            else:
                # save file on server with new name{version}
                title = path.split("/")[-1]
                form = File(title=title, hash_val=hash_val)
                form.save()
                messages.warning(
                    request,
                    "file with same name is already present adding it with new version ",
                )

    return render(request, "utils/upload.html", context)
