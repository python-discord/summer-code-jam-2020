from .forms import FileUploadForm
from .models import MusicFile

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def music_player(request):
    # song_list = MusicFile.objects.filter(
    #     music_owner__user__username=request.user.username
    #     )
    # for song in song_list:
    #     print(song)
    return render(
        request,
        'music_player/music_player.html'
        )


@login_required(login_url='login')
def add_music(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.get('music_musicfile')
            title = request.FILES.get('music_title')
            file_instance = MusicFile(
                music_musicfile=files,
                music_title=title
            )
            file_instance.save()
        messages.success(request, 'music added')
        return redirect('music-home')
    else:
        form = FileUploadForm()
    return render(request, 'music_player/add_music.html', {
        'form': form
        })
