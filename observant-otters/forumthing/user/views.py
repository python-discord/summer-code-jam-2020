from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
@login_required
def profile(request):
    return HttpResponse(f"Hello. You are {request.user.username} (ID {request.user.id}).")
