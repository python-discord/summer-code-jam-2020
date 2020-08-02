from django.shortcuts import render

# Create your views here.

messages = [
    {
        'author': "Evan O'Keefe",
        'content': 'Hey shawty',
        'date_sent': 'August 1st'
    }

]

def home(request):
    context = {
        'messages': messages
    }
    return render(request, 'chat/home.html', context)