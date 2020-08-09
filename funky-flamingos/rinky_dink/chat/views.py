from django.shortcuts import render  # , get_object_or_404
from django.http import Http404, JsonResponse
from .models import Messages  # , Chat

# import json


def index(request):
    # object = get_object_or_404(Chat, slug=slug)
    # context = {"object": object}
    return render(request, "chat/index.html")


def get_messages(request):
    if request.method == "POST":
        return JsonResponse(
            {
                "type": "messages",
                "messages": [
                    {"class_name": "other", "content": "Hello world"},
                    {"class_name": "self", "content": "Hello"},
                ],
                "message": "test",
            }
        )
    raise Http404("Page not found")


def send_message(request):
    if request.method == "POST":
        sent_message = request.POST.get("message", "")  # gets the message sent by user
        if sent_message:
            message = Messages(message=sent_message, sender=request.user)
            print(message)
            message.save()

        return JsonResponse(
            {
                "type": "messages",
                "messages": [{"class_name": "self", "content": sent_message}],
                "message": "test",
            }
        )
    raise Http404("Page not found")
