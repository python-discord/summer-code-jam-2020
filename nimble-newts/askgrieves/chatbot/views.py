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
    return render(
        request, 'home.html'
    )


def chat_page(request, bot_name):
    return render(
        request, 'home.html', {'bot': bot_name}
    )


def experimental(request):
    return render(
        request, 'landing_page.html'
    )