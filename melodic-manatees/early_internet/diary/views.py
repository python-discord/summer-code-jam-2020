from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from diary.forms import DiaryEntryForm
from diary.models import DiaryEntry


@login_required
def diary_entry_list(request):
    object_list = DiaryEntry.objects.all().select_related('creator')
    return render(request, 'diary/list.html', {'object_list': object_list})


@login_required
def diary_entry_detail(request, id):
    obj = get_object_or_404(
        DiaryEntry.objects.select_related('creator'), id=id)
    return render(request, 'diary/detail.html', {'object': obj})


@login_required
def diary_entry_create(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.creator = request.user
            instance.save()
            return redirect('diary-list')
    else:
        form = DiaryEntryForm()

    return render(request, 'diary/create.html', {'form': form})


@login_required
def diary_entry_update(request, id):
    obj = get_object_or_404(
        DiaryEntry.objects.select_related('creator'), id=id)
    form = DiaryEntryForm(instance=obj, data=request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'diary/update.html', {'form': form})


@login_required
def diary_entry_delete(request, id):
    obj = get_object_or_404(
        DiaryEntry.objects.select_related('creator'), id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('/')

    return render(request, 'diary/delete.html', {'object': obj})
