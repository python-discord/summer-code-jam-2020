from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "home.html")


def battle_page(request):
    return render(request, "battle.html")
