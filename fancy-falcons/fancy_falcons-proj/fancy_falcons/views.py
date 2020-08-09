from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {"active_page": "home"})
