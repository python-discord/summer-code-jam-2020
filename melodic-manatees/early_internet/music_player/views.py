from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from django.contrib import messages


def music_player(request):
    return render(request, 'music_player/music_player.html')
    # if request.method == 'POST':
    #     form = ModelFormWithFileField(request.POST, request.FILES)
    #     if form.is_valid():
    #         c.save()
    #         return HttpResponseRedirect('')
    # else:
    #     form = UploadForm()
    # c = {'form': form}
    # c.update(csrf(request))
    # return render(request, 'index.html', {'form': form})


def add_music(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # song_title = request.FILES['song_title']
            form.save()
            # song_obj = form.instance
            return render(request,  'music_player/add_music.html', {'form': form})
    else:
        form = UploadFileForm()
    return render(request,  'music_player/add_music.html', {'form': form})