from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from twilio_messenger.views import sms_send

sample_question = {
    'quiz_id': 1,
    'question': 'What is the airspeed velocity of an unladen swallow?',
    'answers': '1) 3m/s 2) 6m/s 3) 9.81m/s 4) Not enough info'
}

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in as {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def results(request):
    return render(request, 'users/results.html')
