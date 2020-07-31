from django.shortcuts import render


def homepage(request):
    return render(request, 'spydir/home.html')

def info_view(request):
    return render(request, 'spydir/generators/info.html')