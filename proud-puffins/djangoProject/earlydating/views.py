from django.shortcuts import render
from .models import Profile


# Create your views here.
def home(request):
    return render(request, 'dating/home.html')


def login(request):
    return render(request, 'dating/login.html')


def register(request):
    return render(request, 'dating/register.html')


def about(request):
    return render(request, 'dating/about.html')


def DateMatcher(request):
    return render(request, 'dating/DateMatcher.html')


def your_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'dating/YourProfile.html', context)
