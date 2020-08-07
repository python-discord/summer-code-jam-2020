from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from . import models
# Create your views here.


def truth_index(request):
    truths = models.Truth.objects.order_by('-created_at')
    context = {'papers_list': truths}
    return render(request, 'truths/index.html', context)


def truth_post(request, truth_id):
    truth = get_object_or_404(models.Truth, id=truth_id)
    context = {
        'truth': truth
    }
    return render(request, 'truths/truth.html', context)


def upload_truth(request):
    if request.method == 'POST':
        form = models.TruthUploadForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            return HttpResponseRedirect(f'/truths/{saved_post.id}')
        return render(request, 'forum/upload_error.html', {'errors': form.errors})
    return render(request, 'truths/upload.html', {'upload_form': models.TruthUploadForm})
