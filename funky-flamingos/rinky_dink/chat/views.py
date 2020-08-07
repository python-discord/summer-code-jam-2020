from django.shortcuts import render
from django.http import Http404, JsonResponse


def index(request):
    return render(request, "chat/index.html")


def get_messages(request):
    if request.method == "POST":
        return JsonResponse({
            "type": "messages",
            "messages": [{"class_name": "other", "content": "Hello world"}, {"class_name": "self", "content": "Hello"}],
            "message": "test"
        })
    raise Http404("Page not found")
