from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .forms import FileUploadForm, TitleUploadForm
from .models import SongFile
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
    user = request.user
    if request.method == 'POST':
        form = TitleUploadForm(request.POST)
        file_form = FileUploadForm(request.POST, request.FILE)
        files = request.FILES.getlist('song_songfile')
        if form.is_valid() and file_form.is_valid():
            title_instance = form.save(commit=False)
            title_instance.user = user
            title_instance.save()
            for f in files:
                file_instance = SongFile(
                    song_songfile=f, 
                    song_data=title_instance
                    )
                file_instance.save()
        messages.success(request, 'music added')
        return redirect('music_player/music_player.html')
    else:
        form = TitleUploadForm()
        file_form = FileUploadForm()
    return render(request,  'music_player/add_music.html', {
        'form': form,
        'file_form': file_form
        })


# class UploadFileForm(FormView):
#     form_class = UploadFileForm
#     template_name = 'music_player/add_music.html'
#     #success_url = 'music_player/music_player.html'

#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 f.save()
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

