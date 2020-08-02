from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, PhoneNumberForm
from twilio_messenger.views import sms_send

sample_question = 'What is the airspeed velocity of an unladen swallow?'

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
def send(request):
    if request.method == 'POST':
        send_form = PhoneNumberForm(request.POST, instance=request.user)
        if send_form.is_valid():
            send_form.save()
            phonenumbers = send_form.cleaned_data.get('phone_number').__str__()
            sms_send(sample_question, [phonenumbers])
            messages.success(request, 'Your quiz has been sent!')
            return render(request, 'users/results.html',
                {'phonenumbers' : phonenumbers})
        else:
            return render(request, 'users/send.html', {'send_form': send_form})
    else:
        send_form = PhoneNumberForm()
        return render(request, 'users/send.html', {'send_form': send_form} )


@login_required
def results(request):
    return render(request, 'users/results.html')
