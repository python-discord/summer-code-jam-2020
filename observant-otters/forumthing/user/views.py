from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def message(request, id):
    if request.method == "DELETE":
        pass  # @TODO: Handle message deletion

    elif request.method == "PATCH":
        pass  # @TODO: Handle message edit


@login_required
def profile(request):
    return HttpResponse(f"Hello. You are {request.user.username} (ID {request.user.id}).")
