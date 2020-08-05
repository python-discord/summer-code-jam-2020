from .forms import FileUploadForm
from .models import MusicFile

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def music_player(request):
    song_list = MusicFile.objects.filter(music_owner=request.user.userprofile)
    print(len(song_list))
    return render(
        request,
        'music_player/music_player.html',
        {'song_list': song_list}
        )


@login_required(login_url='login')
def add_music(request):
    if request.method == 'POST':
        user = request.user
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.get('music_musicfile')
            title = request.POST.get('music_title')
            file_instance = MusicFile(music_musicfile=files, music_title=title, music_owner=request.user.userprofile)
            file_instance.save()
            messages.success(request, 'music added')
            return redirect('music-home')
    else:
        form = FileUploadForm()
    return render(request, 'music_player/add_music.html', {
        'form': form
        })

@login_required(login_url='login')
def delete_music(request, pk):
    to_be_deleted_music_file = MusicFile.objects.get(pk=pk)
    print(to_be_deleted_music_file.pk)
    if request.method == 'POST':
        to_be_deleted_music_file.delete()
        return redirect('music-home')
    return redirect('music-home')


@login_required(login_url='login')
def use_music(request, pk):
    to_be_used_music_file = MusicFile.objects.get(pk=pk)
    if request.method == 'POST':
        print(f'music file to be used {to_be_used_music_file.music_title}')
        return redirect('music-home')
    return redirect('music-home')

