from .forms import FileUploadForm
from .models import BackgroundFile
from users.models import UserProfile
from . import background_utility
import os
from django.core.files import File
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def background_home(request):
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
            files = request.FILES.get('background_file')
            title = request.POST.get('background_title')
            if background_utility.resolution_checker(files.temporary_file_path()):
                file_instance = BackgroundFile(
                    background_file=files,
                    background_title=title,
                    background_owner=request.user.profile
                    )
                file_instance.save()
                thumbnail_path = background_utility.image_resizer(file_instance.background_file.path)
                file_instance.background_thumbnail.save(f'{file_instance.background_title}_{file_instance.id}_thumbnail', File(open(f'{thumbnail_path}', 'rb'))) 
                file_instance.save()
                if os.path.exists(f'{os.path.splitext(file_instance.background_file.path)[0]}_thumbnail'):
                    os.remove(f'{os.path.splitext(file_instance.background_file.path)[0]}_thumbnail')
                messages.success(request, 'background added')
                return redirect('background-home')
            else:
                messages.error(request, "image size too large")
                return redirect('add-background')
        else:
            file_instance.delete()
            messages.error(request, "image resolution too low")
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
    to_be_deleted_background = BackgroundFile.objects.get(pk=pk)
    if request.method == 'POST':
        # print(to_be_deleted_background.background_thumbnail)
        # to_be_deleted_background.background_thumbnail.delete()
        to_be_deleted_background.delete()
        messages.success(request, 'background image deleted')
        return redirect('background-home')
    return redirect('background-home')


@login_required(login_url='login')
def use_background(request, pk):
    to_be_used_background_file = BackgroundFile.objects.get(pk=pk)
    if request.method == 'POST':
        UserProfile.background_image = to_be_used_background_file.background_file
        messages.success(request, f'background changed to {to_be_used_background_file.background_title}')
        return redirect('background-home')
    return redirect('background-home')
