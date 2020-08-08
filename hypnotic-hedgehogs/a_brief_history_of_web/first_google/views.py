from django.shortcuts import render, redirect
from pathlib import PurePath


# Create your views here.
def index(request):

    index_path = PurePath('first_google/index.html')
    return render(request, index_path)


def results(request, search_text):
    context = {"search_text": search_text}
    results_path = PurePath('first_google/results.html')
    return render(request, results_path, context)
