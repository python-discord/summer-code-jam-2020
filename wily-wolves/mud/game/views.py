# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")


def register(request):
    return HttpResponse("This is the register page.")
