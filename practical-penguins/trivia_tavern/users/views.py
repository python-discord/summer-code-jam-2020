from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, PhoneNumberForm
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
def send(request):
    """Core logic of the send view. If the user posts a valid phone number,
    send quiz and answers, otherwise reload the form
    """
    if request.method == 'POST':
        send_form = PhoneNumberForm(request.POST, instance=request.user)
        if send_form.is_valid():
            send_form.save()
            # in the future, we will have multiple form inputs, and this will
            # be a list
            phonenumbers = send_form.cleaned_data.get('phone_number').__str__()
            # @[phonenumbers] temporary hack so numbers are processed as a list
            sms_send(sample_question['question'], [phonenumbers])
            sms_send(sample_question['answers'], [phonenumbers])
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
