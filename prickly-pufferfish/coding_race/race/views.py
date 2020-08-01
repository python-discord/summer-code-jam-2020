from django.shortcuts import render

def home(request):
    return render(request,'race/home.html')
# Create your views here.
