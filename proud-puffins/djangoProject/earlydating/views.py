from django.shortcuts import render
from .models import Profile


# Create your views here.
def home(request):
    return render(request, 'dating/home.html')


def about(request):
    return render(request, 'dating/about.html')


def your_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'dating/YourProfile.html', context)
