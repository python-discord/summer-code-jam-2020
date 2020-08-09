from django.shortcuts import render

# Create your views here.

def gamepage(request):

    context = {
        "login": request.user.is_authenticated,
        "page": "game"
    }

    return render(request, "game.html", context)
