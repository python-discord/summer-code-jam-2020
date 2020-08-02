from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'chat/home.html')

def bot(request):
    return render(request, 'chat/bot.html')
