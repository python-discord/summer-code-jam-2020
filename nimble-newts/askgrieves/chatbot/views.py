from django.http import HttpResponse
from django.shortcuts import render


class Message:
    send = True

    def __init__(self, text):
        if Message.send:
            self.action = 'send'
        else:
            self.action = 'receive'
        Message.send = not self.send
        self.text = text

# Create your views here.

def home(request):
    messages = [
        'Hi',
        'Hello',
        'Are you waiting for the bus?',
        'Yes Im waiting for the bus',
        'I notice youre not wearing any gollashes',
    ]
    return render(
        request, 'home.html', {f'message_list': [Message(s) for s in messages]}
    )
