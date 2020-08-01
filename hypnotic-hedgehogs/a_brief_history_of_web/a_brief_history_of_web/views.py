from django.shortcuts import render
from pathlib import PurePath


def index(request):
    # index_path = PurePath('a_brief_history_of_web/index.html')
    index_path = 'a_brief_history_of_web/index.html'

    return render(request, index_path)
