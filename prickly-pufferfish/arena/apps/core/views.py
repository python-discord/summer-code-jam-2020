from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "home.html")


def battle_page(request):
    return render(request, "battle.html")


def about_page(request):
    return render(request, "about_page.html")
