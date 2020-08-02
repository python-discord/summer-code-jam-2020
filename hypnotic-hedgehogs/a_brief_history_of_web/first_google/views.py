from django.http import HttpResponse
from django.shortcuts import render
from pathlib import PurePath


# Create your views here.
def index(requests):
    index_path = PurePath('first_google/index.html')
    return render(requests, index_path)
