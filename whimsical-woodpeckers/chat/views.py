from django.shortcuts import render
from .models import Texts


def home(request):
    context = {
        'texts': Texts.objects.all()
    }
    return render(request, 'chat/home.html', context)