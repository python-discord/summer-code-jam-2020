from django.shortcuts import render


def main_hub(request):
    return render(request, 'home.html')
