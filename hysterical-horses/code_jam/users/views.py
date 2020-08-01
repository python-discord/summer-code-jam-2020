from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def profile(request):
    context = {'user_form': None, 'profile_form': None}
    return render(request, 'users/profile.html', context)
