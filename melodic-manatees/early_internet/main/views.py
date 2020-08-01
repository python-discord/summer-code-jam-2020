from django.shortcuts import render


def main(request):
    return render(request, 'main/main-base.html')


def about(request):
    return render(request, 'main/main-about.html')
