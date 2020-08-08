from django.shortcuts import render
from django.http import Http404, JsonResponse
from .models import Messages
import json


def index(request):
    return render(request, "chat/index.html")


def get_messages(request):
    sent_message = request.GET.get('sent_message', '') # json object
    message = json.load(sent_message)['message']
    # print(sent_message)
    # print(request.POST)
    message = Messages(message=sent_message, sender=request.user)
    # print(message)
    message.save()
    # message.recipent.add(?recipent?)

    if request.method == "POST":
        return JsonResponse({
            "type": "messages",
            "messages": [{"class_name": "other", "content": "Hello world"}, {"class_name": "self", "content": "Hello"}],
            "message": "test"
        })
    raise Http404("Page not found")
