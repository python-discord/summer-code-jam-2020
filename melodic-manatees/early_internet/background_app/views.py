from .forms import FileUploadForm
from .models import BackgroundFile
from users.models import UserProfile
from . import background_utility
import os
from django.core.files import File
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

'''All background related views go here'''


def background_home(request):
    # get all background objects associated with this user,
    # and pass them as context to the HTML page
    background_list = BackgroundFile.objects.filter(
        background_owner=request.user.profile
    )
    print(len(background_list))
    return render(
        request,
        'background_app/background_home.html',
        {'background_list': background_list}
    )


@login_required(login_url='login')
def add_background(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # get title and file from the request object
            files = request.FILES.get('background_file')
            title = request.POST.get('background_title')
            file_instance = BackgroundFile(
                background_file=files,
                background_title=title,
                background_owner=request.user.profile
            )
            file_instance.save()
            # pass the file to the resolution checker
            if background_utility.resolution_checker(
                file_instance.background_file.path
            ):
            # create a thumbnail and save it in the instance model
                thumbnail_path = background_utility.image_resizer(
                    file_instance.background_file.path
                )
                file_instance.background_thumbnail.save(
                    f'{file_instance.background_title}_{file_instance.id}_thumbnail',
                    File(open(f'{thumbnail_path}', 'rb'))
                )
                file_instance.save()
                # remove thumbnail created by the image resizer
                if os.path.exists(f'{os.path.splitext(file_instance.background_file.path)[0]}_thumbnail'):
                    os.remove(f'{os.path.splitext(file_instance.background_file.path)[0]}_thumbnail')
                messages.success(request, 'background added')
                return redirect('background-home')
            else:
                file_instance.delete()
                # image resolution must be at least 1200*800
                messages.error(request, "image resolution too low")
                return redirect('add-background')
        else:
            # FileUploadHandler cannot parse images more than 2.5MB,
            # that requires the TempHandler
            messages.error(request, "images must be less than 2.5MB")
            return redirect('add-background')
    else:
        form = FileUploadForm()
    return render(
        request,
        'background_app/add_background.html',
        {
            'form': form
        }
    )


@login_required(login_url='login')
def delete_background(request, pk):
    '''function called when the delete button is pressed'''
    session = UserProfile.objects.get(user=request.user)
    to_be_deleted_background = BackgroundFile.objects.get(pk=pk)
    if request.method == 'POST':
        default = open('media/defaults/sunrise.jpg', 'rb')
        to_be_deleted_background.delete()
        session.background_image.save('default', File(default))
        messages.success(request, 'background image deleted')
        return redirect('background-home')
    return redirect('background-home')


@login_required(login_url='login')
def use_background(request, pk):
    ''' if background selected, change user profile background_image field'''
    session = UserProfile.objects.get(user=request.user)
    to_be_used_background_file = BackgroundFile.objects.get(pk=pk)
    if request.method == 'POST':
        session.background_image.save(to_be_used_background_file.background_title, to_be_used_background_file.background_file)
        messages.success(
            request,
            f'background changed to {to_be_used_background_file.background_title}'
        )
        return redirect('background-home')
    return redirect('background-home')
