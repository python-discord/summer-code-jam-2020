from django.shortcuts import render 
from django.http import Http404, JsonResponse
from .models import Messages


def index(request):
    return render(request, "chat/index.html")


def get_messages(request):
    messages = Messages.objects.all().order_by('-time')[:50]  # to get last 50 messages
    messages = reversed(messages)
    if request.method == "POST":
        return_val = {
            "type": "messages",
            "messages": [],
        }

        for message in messages:
            print(message)
            if message.sender == request.user:
                class_name = "self"
            else:
                class_name = "other"
            return_val["messages"].append({
                "class_name": class_name,
                "content": message.message,
                "username": message.sender.username
            })

        return JsonResponse(return_val)
    raise Http404("Page not found")


def send_message(request):
    if request.method == "POST":
        sent_message = request.POST.get("message", "")  # gets the message sent by user
        if sent_message:
            message = Messages(message=sent_message, sender=request.user)
            print(message)
            message.save()

        messages = Messages.objects.all().order_by('-time')[:50]  # to get last 50 messages
        messages = reversed(messages)
        return_val = {
            "type": "messages",
            "messages": [],
        }

        for message in messages:
            print(message)
            if message.sender == request.user:
                class_name = "self"
            else:
                class_name = "other"
            return_val["messages"].append({
                "class_name": class_name,
                "content": message.message,
                "username": message.sender.username
            })

        return JsonResponse(return_val)
    raise Http404("Page not found")
