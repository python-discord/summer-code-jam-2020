from django.shortcuts import render
from .models import Profile
from .forms import CreateUserForm


# Create your views here.
def home(request):
    return render(request, 'dating/home.html')


def login(request):
    return render(request, 'dating/login.html')


def register(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'dating/register.html', context)


def about(request):
    return render(request, 'dating/about.html')


def DateMatcher(request):
    return render(request, 'dating/DateMatcher.html')


def your_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'dating/YourProfile.html', context)
