from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Texts


def home(request):
    return render(request, 'chat/home.html')

@login_required
def chat(request):
    context = {
        'texts': Texts.objects.all()
    }
    return render(request, 'chat/chat.html', context)